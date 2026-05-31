<template>
  <div>

    <div class="topbar">
      <div>
        <h1>My Applications</h1>
        <p>Track all your placement applications • {{ applications.length }} total</p>
      </div>
      <input
        v-model="search"
        class="search-input"
        type="text"
        placeholder="Search by company or drive..."
      />
    </div>

    <!-- ✅ Loading state -->
    <div v-if="loading" class="empty" style="padding: 60px 0;">
      Loading applications...
    </div>

    <div v-else class="table-box">
      <table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Company</th>
            <th>Role / Drive</th>
            <th>Applied On</th>
            <th>Package</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(app, index) in filteredApplications" :key="app.id">
            <td>{{ index + 1 }}</td>
            <td>{{ app.company }}</td>
            <td>{{ app.drive }}</td>
            <td>{{ app.date }}</td>
            <td>{{ app.package || '—' }}</td>
            <td>
              <span :class="getStatusClass(app.status)">
                {{ app.status }}
              </span>
            </td>
            <td>
              <button class="btn-view" @click="viewDetail(app)">View Details</button>
            </td>
          </tr>
        </tbody>
      </table>

      <div v-if="filteredApplications.length === 0" class="empty">
        No applications found
      </div>
    </div>

    <!-- ✅ Modal -->
    <div v-if="selectedApp" class="modal-overlay" @click.self="selectedApp = null">
      <div class="modal">

        <div class="modal-header">
          <h3>Application Detail</h3>
          <button class="btn-close" @click="selectedApp = null">✕</button>
        </div>

        <div v-if="modalLoading" class="empty" style="padding: 40px 0;">
          Loading detail...
        </div>

        <div v-else>
          <div class="detail-top">
            <div class="avatar-lg">{{ selectedApp.student_name ? selectedApp.student_name.charAt(0) : '?' }}</div>
            <div>
              <h4>{{ selectedApp.student_name }}</h4>
              <p>{{ selectedApp.company }} · {{ selectedApp.drive }}</p>
            </div>
            <span :class="getStatusClass(selectedApp.status)">{{ selectedApp.status }}</span>
          </div>

          <div class="detail-rows">
            <div class="detail-row">
              <span class="detail-label">Student Name</span>
              <span class="detail-value">{{ selectedApp.student_name || '—' }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Email</span>
              <span class="detail-value">{{ selectedApp.email || '—' }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Company</span>
              <span class="detail-value">{{ selectedApp.company || '—' }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Role</span>
              <span class="detail-value">{{ selectedApp.drive || '—' }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Package</span>
              <span class="detail-value">{{ selectedApp.package || '—' }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Applied On</span>
              <span class="detail-value">{{ selectedApp.date || '—' }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Status</span>
              <span :class="getStatusClass(selectedApp.status)">{{ selectedApp.status }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Feedback</span>
              <span class="detail-value">{{ selectedApp.feedback || 'N/A' }}</span>
            </div>
            <div class="detail-row" v-if="selectedApp.resume">
              <span class="detail-label">Resume</span>
              <a :href="selectedApp.resume" target="_blank" class="resume-link">📄 View Resume</a>
            </div>
          </div>

          <div class="modal-footer">
            <button class="btn-close-modal" @click="selectedApp = null">Close</button>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "StudentApplicationsView",

  data() {
    return {
      loading:      true,
      modalLoading: false,
      search:       "",
      selectedApp:  null,
      applications: [],
    }
  },

  async mounted() {
    await this.fetchApplications()
  },

  computed: {
    filteredApplications() {
      const q = this.search.toLowerCase()
      return this.applications.filter(app =>
        app.company.toLowerCase().includes(q) ||
        app.drive.toLowerCase().includes(q)
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

    getStatusClass(status) {
      if (status === 'Selected')    return 'badge-selected'
      if (status === 'Shortlisted') return 'badge-shortlisted'
      if (status === 'Rejected')    return 'badge-rejected'
      return 'badge-applied'
    },

    async fetchApplications() {
      this.loading = true
      try {
        const res = await axios.get("http://localhost:5000/student/my_applications", this.getHeaders())
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
      try {
        const res = await axios.get(`http://localhost:5000/student/application_detail/${app.id}`, this.getHeaders())
        const d = res.data
        this.selectedApp = {
          ...app,
          feedback     : d.feedback,
          resume       : d.resume,
        }
      } catch (err) {
        console.error("Application detail load failed:", err)
      } finally {
        this.modalLoading = false
      }
    }
  }
}
</script>

<style scoped>

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
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

.badge-selected {
  background: #dcfce7;
  color: #16a34a;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.badge-shortlisted {
  background: #fef9c3;
  color: #ca8a04;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.badge-rejected {
  background: #fee2e2;
  color: #dc2626;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.badge-applied {
  background: #dbeafe;
  color: #2563eb;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
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
  width: 620px;
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
  margin-bottom: 24px;
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

.modal-footer {
  display: flex;
  justify-content: flex-end;
}

.btn-close-modal {
  background: #f3f4f6;
  color: #374151;
  border: none;
  padding: 9px 18px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-close-modal:hover {
  background: #e5e7eb;
}

</style>