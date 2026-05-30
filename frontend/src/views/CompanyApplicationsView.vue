<template>
  <div class="applications-page">

    <div class="topbar">
      <div>
        <h1>Applications</h1>
        <p>All applications for your drives</p>
      </div>
      <input
        v-model="search"
        type="text"
        placeholder="Search by student, drive or status..."
        class="search-input"
      />
    </div>

    <div v-if="loading" class="empty" style="padding: 60px 0;">
      Loading applications...
    </div>

    <div v-else class="table-box">
      <table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Student</th>
            <th>Drive</th>
            <th>Applied On</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(application, index) in filteredApplications" :key="application.id">
            <td>{{ index + 1 }}</td>
            <td>{{ application.student_name }}</td>
            <td>{{ application.drive_title }}</td>
            <td>{{ application.apply_date }}</td>
            <td>
              <span :class="[
                'status-badge',
                application.status === 'Pending'     ? 'status-pending'     :
                application.status === 'Shortlisted' ? 'status-shortlisted' :
                application.status === 'Rejected'    ? 'status-rejected'    :
                'status-selected'
              ]">{{ application.status }}</span>
            </td>
            <td>
              <div class="actions">
                <button class="btn-view" @click="viewDetail(application)">View Details</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <div v-if="filteredApplications.length === 0" class="empty">
        No applications found
      </div>
    </div>

    <div v-if="selectedApp" class="modal-overlay" @click.self="closeModal">
      <div class="modal">

        <div class="modal-header">
          <h3>Application Detail</h3>
          <button class="btn-close" @click="closeModal">✕</button>
        </div>

        <div v-if="modalLoading" class="empty" style="padding: 40px 0;">
          Loading detail...
        </div>

        <div v-else>
          <div class="detail-top">
            <div class="avatar-lg">{{ selectedApp.student_name ? selectedApp.student_name.charAt(0) : '?' }}</div>
            <div>
              <h4>{{ selectedApp.student_name }}</h4>
              <p>CGPA {{ selectedApp.cgpa }}</p>
            </div>
            <span :class="[
              'status-badge',
              selectedApp.status === 'Pending'     ? 'status-pending'     :
              selectedApp.status === 'Shortlisted' ? 'status-shortlisted' :
              selectedApp.status === 'Rejected'    ? 'status-rejected'    :
              'status-selected'
            ]">{{ selectedApp.status }}</span>
          </div>

          <div class="detail-rows">
            <div class="detail-row">
              <span class="detail-label">Drive</span>
              <span class="detail-value">{{ selectedApp.drive_name }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Applied On</span>
              <span class="detail-value">{{ selectedApp.apply_date }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Email</span>
              <span class="detail-value">{{ selectedApp.email }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Skills</span>
              <span class="detail-value">{{ selectedApp.skills || '—' }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Bio</span>
              <span class="detail-value">{{ selectedApp.bio || '—' }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Resume</span>
              <a v-if="selectedApp.resume" :href="selectedApp.resume" target="_blank" class="resume-link">📄 View Resume</a>
              <span v-else class="detail-value">—</span>
            </div>
          </div>

          <div class="feedback-section">
            <label class="feedback-label">Feedback</label>
            <textarea
              v-model="feedback"
              class="feedback-input"
              placeholder="Write feedback for this student..."
              rows="3"
            ></textarea>
          </div>

          <div class="modal-actions">
            <button class="btn-shortlist" @click="updateStatus('Shortlisted')">
              ✓ Shortlist
            </button>
            <button class="btn-reject" @click="updateStatus('Rejected')">
              ✕ Reject
            </button>
            <button class="btn-feedback" @click="saveFeedback">
              💬 Save Feedback
            </button>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "CompanyApplicationsView",

  data() {
    return {
      loading:      true,
      modalLoading: false,
      search:       "",
      selectedApp:  null,
      feedback:     "",
      applications: [],
    }
  },

  async mounted() {
    await this.fetchApplications()
  },

  computed: {
    filteredApplications() {
      const q = this.search.toLowerCase()
      return this.applications.filter(a =>
        a.student_name.toLowerCase().includes(q) ||
        a.drive_title.toLowerCase().includes(q)  ||
        a.status.toLowerCase().includes(q)
      )
    }
  },

  methods: {

    getHeaders() {
      return {
        headers: {
          "Authentication-Token": localStorage.getItem("token"),
        },
      }
    },

    async fetchApplications() {
      this.loading = true
      try {
        const res = await axios.get("http://localhost:5000/company/dashboard_data", this.getHeaders())
        this.applications = res.data.applications || []
      } catch (err) {
        console.error("Applications load failed:", err)
      } finally {
        this.loading = false
      }
    },

    async viewDetail(app) {
      this.selectedApp  = app
      this.modalLoading = true
      this.feedback     = ""
      try {
        const res = await axios.get(`http://localhost:5000/company/application_detail/${app.id}`, this.getHeaders())
        this.selectedApp = res.data
        this.feedback    = res.data.feedback || ""
      } catch (err) {
        console.error("Application detail load failed:", err)
      } finally {
        this.modalLoading = false
      }
    },

    async updateStatus(status) {
      try {
        await axios.patch(
          `http://localhost:5000/company/application_update/${this.selectedApp.id}`,
          { status: status, feedback: this.feedback },
          this.getHeaders()
        )
        const app = this.applications.find(a => a.id === this.selectedApp.id)
        if (app) app.status = status
        this.closeModal()
      } catch (err) {
        console.error("Status update failed:", err)
      }
    },

    async saveFeedback() {
      try {
        await axios.patch(
          `http://localhost:5000/company/application_update/${this.selectedApp.id}`,
          { status: this.selectedApp.status, feedback: this.feedback },
          this.getHeaders()
        )
        alert("Feedback saved successfully! ✅")
      } catch (err) {
        console.error("Feedback save failed:", err)
      }
    },

    closeModal() {
      this.selectedApp = null
      this.feedback    = ""
    }
  }
}
</script>

<style scoped>

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.applications-page {
  width: 100%;
}

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  flex-wrap: wrap;
  gap: 20px;
}

.topbar h1 {
  font-size: 34px;
  color: #111827;
  margin-bottom: 4px;
}

.topbar p {
  color: #6b7280;
  font-size: 15px;
}

.search-input {
  padding: 11px 14px;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  font-size: 14px;
  color: #111827;
  width: 280px;
  outline: none;
  transition: 0.2s;
  background: white;
}

.search-input:focus {
  border-color: #2563eb;
}

.table-box {
  background: white;
  border-radius: 18px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  overflow: hidden;
}

table {
  width: 100%;
  border-collapse: collapse;
}

thead {
  background: #f9fafb;
}

th {
  padding: 16px 20px;
  text-align: left;
  font-size: 14px;
  color: #6b7280;
  font-weight: 600;
  border-bottom: 1px solid #e5e7eb;
}

td {
  padding: 16px 20px;
  font-size: 15px;
  color: #111827;
  border-bottom: 1px solid #f3f4f6;
  font-weight: 600;
}

tr:last-child td {
  border-bottom: none;
}

tr:hover td {
  background: #f9fafb;
}

.actions {
  display: flex;
  gap: 10px;
  align-items: center;
}

.btn-view {
  background: #eff6ff;
  color: #2563eb;
  border: none;
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-view:hover {
  background: #dbeafe;
}

.status-badge {
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
  white-space: nowrap;
}

.status-pending {
  background: #fef9c3;
  color: #ca8a04;
}

.status-shortlisted {
  background: #dbeafe;
  color: #2563eb;
}

.status-rejected {
  background: #fee2e2;
  color: #dc2626;
}

.status-selected {
  background: #dcfce7;
  color: #16a34a;
}

.empty {
  text-align: center;
  color: #9ca3af;
  font-size: 15px;
  padding: 40px 0;
}

.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal {
  background: white;
  border-radius: 18px;
  width: 580px;
  max-width: 90%;
  max-height: 85vh;
  overflow-y: auto;
  padding: 28px;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  position: sticky;
  top: 0;
  background: white;
  z-index: 1;
  padding-bottom: 16px;
  border-bottom: 1px solid #f3f4f6;
}

.modal-header h3 {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
}

.btn-close {
  background: #f3f4f6;
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  font-size: 14px;
  cursor: pointer;
  color: #374151;
}

.detail-top {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 20px;
  padding-bottom: 16px;
  border-bottom: 1px solid #f3f4f6;
}

.avatar-lg {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: #eff6ff;
  color: #2563eb;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 22px;
  font-weight: 700;
  flex-shrink: 0;
}

.detail-top h4 {
  font-size: 16px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 4px;
  flex: 1;
}

.detail-top p {
  font-size: 13px;
  color: #6b7280;
}

.detail-rows {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 20px;
}

.detail-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
  padding-bottom: 10px;
  border-bottom: 1px solid #f3f4f6;
}

.detail-label { 
  color: #6b7280; 
}

.detail-value {
  color: #111827;
  font-weight: 600;
  text-align: right;
  max-width: 60%;
  word-break: break-word;
}

.resume-link {
  color: #2563eb;
  font-weight: 600;
  font-size: 14px;
  text-decoration: none;
}

.resume-link:hover {
  text-decoration: underline;
}

.feedback-section {
  margin-bottom: 20px;
}

.feedback-label {
  display: block;
  font-size: 14px;
  color: #6b7280;
  margin-bottom: 8px;
  font-weight: 500;
}

.feedback-input {
  width: 100%;
  padding: 12px 14px;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  font-size: 14px;
  color: #111827;
  outline: none;
  resize: none;
  transition: 0.2s;
  font-family: inherit;
  box-sizing: border-box;
}

.feedback-input:focus {
  border-color: #2563eb;
}

.modal-actions {
  display: flex;
  gap: 10px;
}

.btn-shortlist {
  flex: 1;
  padding: 11px;
  background: #dbeafe;
  color: #2563eb;
  border: none;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-shortlist:hover { 
  background: #bfdbfe; 
}

.btn-reject {
  flex: 1;
  padding: 11px;
  background: #fee2e2;
  color: #dc2626;
  border: none;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-reject:hover { 
  background: #fecaca; 
}

.btn-feedback {
  flex: 1;
  padding: 11px;
  background: #f3f4f6;
  color: #374151;
  border: none;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-feedback:hover { 
  background: #e5e7eb; 
}
</style>