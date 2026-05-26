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

    <div class="table-box">
      <table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Student</th>
            <th>Drive</th>
            <th>Applied On</th>
            <th>Branch</th>
            <th>CGPA</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(application, index) in filteredApplications" :key="application.id">
            <td>{{ index + 1 }}</td>
            <td>{{ application.student }}</td>
            <td>{{ application.drive }}</td>
            <td>{{ application.apply_date }}</td>
            <td>{{ application.branch }}</td>
            <td>{{ application.cgpa }}</td>
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

        <div class="detail-top">
          <div class="avatar-lg">{{ selectedApp.student.charAt(0) }}</div>
          <div>
            <h4>{{ selectedApp.student }}</h4>
            <p>{{ selectedApp.branch }} · CGPA {{ selectedApp.cgpa }}</p>
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
            <span class="detail-value">{{ selectedApp.drive }}</span>
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
            <span class="detail-label">Phone</span>
            <span class="detail-value">{{ selectedApp.phone }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">College</span>
            <span class="detail-value">{{ selectedApp.college }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Skills</span>
            <span class="detail-value">{{ selectedApp.skills }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Resume</span>
            <a :href="selectedApp.resume" target="_blank" class="resume-link">📄 View Resume</a>
          </div>
        </div>

        <div class="feedback-section">
          <label class="feedback-label">Feedback</label>
          <textarea
            v-model="selectedApp.feedback"
            class="feedback-input"
            placeholder="Write feedback for this student..."
            rows="3"
          ></textarea>
        </div>

        <div class="modal-actions">
          <button class="btn-shortlist" @click="updateStatus(selectedApp, 'Shortlisted')">
            ✓ Shortlist
          </button>
          <button class="btn-reject" @click="updateStatus(selectedApp, 'Rejected')">
            ✕ Reject
          </button>
          <button class="btn-feedback" @click="saveFeedback(selectedApp)">
            💬 Save Feedback
          </button>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "CompanyApplicationsView",

  data() {
    return {
      search: "",
      selectedApp: null,
      applications: [
        { id: 1, student: "Rahul Sharma", drive: "Software Engineer",    apply_date: "10 May 2026", branch: "CSE", cgpa: "8.9", email: "rahul@college.com",  phone: "+91 9876543210", college: "IIT Delhi",   skills: "Vue, Python, Java",  resume: "#", feedback: "", status: "Pending"  },
        { id: 2, student: "Priya Singh",  drive: "Frontend Developer",   apply_date: "11 May 2026", branch: "ECE", cgpa: "7.5", email: "priya@college.com",  phone: "+91 9876543211", college: "NIT Trichy",  skills: "React, CSS, HTML",   resume: "#", feedback: "", status: "Shortlisted" },
        { id: 3, student: "Amit Kumar",   drive: "Backend Developer",    apply_date: "12 May 2026", branch: "ME",  cgpa: "8.1", email: "amit@college.com",   phone: "+91 9876543212", college: "VIT Vellore", skills: "Node.js, MongoDB",   resume: "#", feedback: "", status: "Rejected" },
        { id: 4, student: "Sneha Verma",  drive: "Software Engineer",    apply_date: "13 May 2026", branch: "CSE", cgpa: "9.2", email: "sneha@college.com",  phone: "+91 9876543213", college: "IIT Bombay",  skills: "Java, Spring Boot",  resume: "#", feedback: "", status: "Pending"  },
        { id: 5, student: "Rohan Gupta",  drive: "Full Stack Developer", apply_date: "14 May 2026", branch: "IT",  cgpa: "7.8", email: "rohan@college.com",  phone: "+91 9876543214", college: "BITS Pilani", skills: "Vue, Node, MySQL",   resume: "#", feedback: "", status: "Pending"  },
        { id: 6, student: "Pooja Yadav",  drive: "Frontend Developer",   apply_date: "15 May 2026", branch: "CSE", cgpa: "8.4", email: "pooja@college.com",  phone: "+91 9876543215", college: "IIT Madras",  skills: "React, Tailwind",    resume: "#", feedback: "", status: "Shortlisted" },
      ]
    }
  },

  computed: {
    filteredApplications() {
      const q = this.search.toLowerCase()
      return this.applications.filter(a =>
        a.student.toLowerCase().includes(q) ||
        a.drive.toLowerCase().includes(q)   ||
        a.status.toLowerCase().includes(q)
      )
    }
  },

  methods: {
    viewDetail(app) {
      this.selectedApp = app
    },
    closeModal() {
      this.selectedApp = null
    },
    updateStatus(app, status) {
      app.status = status
      this.selectedApp = null
    },
    saveFeedback(app) {
      alert(`Feedback saved for ${app.student}!`)
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

.detail-label { color: #6b7280; }

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