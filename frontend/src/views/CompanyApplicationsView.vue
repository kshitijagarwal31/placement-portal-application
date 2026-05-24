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

    <div class="applications-grid">
      <div
        class="application-card"
        v-for="application in filteredApplications"
        :key="application.id"
      >
        <div class="card-top">
          <div class="avatar">{{ application.student.charAt(0) }}</div>
          <div class="card-info">
            <h2>{{ application.student }}</h2>
            <p class="drive-name">{{ application.drive }}</p>
          </div>
          <span :class="[
            'status-badge',
            application.status === 'Pending'   ? 'status-pending'   :
            application.status === 'Selected'  ? 'status-selected'  :
            'status-rejected'
          ]">{{ application.status }}</span>
        </div>

        <div class="card-details">
          <div class="detail-item">
            <p class="detail-label">Applied On</p>
            <h4>{{ application.apply_date }}</h4>
          </div>
          <div class="detail-item">
            <p class="detail-label">Branch</p>
            <h4>{{ application.branch }}</h4>
          </div>
          <div class="detail-item">
            <p class="detail-label">CGPA</p>
            <h4>{{ application.cgpa }}</h4>
          </div>
        </div>

        <button class="view-btn" @click="viewDetail(application)">View Details</button>

      </div>
    </div>

    <div v-if="filteredApplications.length === 0" class="empty">
      No applications found
    </div>

    <div v-if="selectedApp" class="modal-overlay" @click.self="selectedApp = null">
      <div class="modal">

        <div class="modal-header">
          <h3>Application Detail</h3>
          <button class="btn-close" @click="selectedApp = null">✕</button>
        </div>

        <div class="modal-body">

          <div class="detail-top">
            <div class="avatar-lg">{{ selectedApp.student.charAt(0) }}</div>
            <div>
              <h4>{{ selectedApp.student }}</h4>
              <p>{{ selectedApp.branch }} · CGPA {{ selectedApp.cgpa }}</p>
            </div>
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
              <span class="detail-label">Skills</span>
              <span class="detail-value">{{ selectedApp.skills }}</span>
            </div>
            <div class="detail-row">
              <span class="detail-label">Status</span>
              <span :class="[
                'status-badge',
                selectedApp.status === 'Pending'  ? 'status-pending'  :
                selectedApp.status === 'Selected' ? 'status-selected' :
                'status-rejected'
              ]">{{ selectedApp.status }}</span>
            </div>
          </div>

          <div class="modal-actions">
            <button class="btn-select" @click="updateStatus(selectedApp, 'Selected')">Select</button>
            <button class="btn-reject" @click="updateStatus(selectedApp, 'Rejected')">Reject</button>
          </div>

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
        { id: 1, student: "Rahul Sharma",  drive: "Software Engineer",    apply_date: "10 May 2026", branch: "CSE", cgpa: "8.9", email: "rahul@college.com",  phone: "+91 9876543210", skills: "Vue, Python, Java",  status: "Pending"  },
        { id: 2, student: "Priya Singh",   drive: "Frontend Developer",   apply_date: "11 May 2026", branch: "ECE", cgpa: "7.5", email: "priya@college.com",  phone: "+91 9876543211", skills: "React, CSS, HTML",   status: "Selected" },
        { id: 3, student: "Amit Kumar",    drive: "Backend Developer",    apply_date: "12 May 2026", branch: "ME",  cgpa: "8.1", email: "amit@college.com",   phone: "+91 9876543212", skills: "Node.js, MongoDB",   status: "Rejected" },
        { id: 4, student: "Sneha Verma",   drive: "Software Engineer",    apply_date: "13 May 2026", branch: "CSE", cgpa: "9.2", email: "sneha@college.com",  phone: "+91 9876543213", skills: "Java, Spring Boot",  status: "Pending"  },
        { id: 5, student: "Rohan Gupta",   drive: "Full Stack Developer", apply_date: "14 May 2026", branch: "IT",  cgpa: "7.8", email: "rohan@college.com",  phone: "+91 9876543214", skills: "Vue, Node, MySQL",   status: "Pending"  },
        { id: 6, student: "Pooja Yadav",   drive: "Frontend Developer",   apply_date: "15 May 2026", branch: "CSE", cgpa: "8.4", email: "pooja@college.com",  phone: "+91 9876543215", skills: "React, Tailwind",    status: "Selected" },
      ]
    }
  },

  computed: {
    filteredApplications() {
      const q = this.search.toLowerCase()
      return this.applications.filter(a =>
        a.student.toLowerCase().includes(q) ||
        a.drive.toLowerCase().includes(q)  ||
        a.status.toLowerCase().includes(q)
      )
    }
  },

  methods: {
    viewDetail(app) {
      this.selectedApp = app
    },
    updateStatus(app, status) {
      app.status = status
      this.selectedApp = null
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
  gap: 20px;
  margin-bottom: 28px;
  flex-wrap: wrap;
}

.topbar h1 {
  font-size: 30px;
  color: #111827;
  margin-bottom: 4px;
}

.topbar p {
  color: #6b7280;
  font-size: 14px;
}

.search-input {
  width: 260px;
  padding: 11px 14px;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  outline: none;
  font-size: 14px;
  transition: 0.2s;
  background: white;
}

.search-input:focus {
  border-color: #2563eb;
}

.applications-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
}

.application-card {
  background: white;
  border-radius: 18px;
  padding: 20px;
  border: 1px solid #f1f5f9;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 220px;
  transition: 0.2s;
}

.application-card:hover {
  transform: translateY(-3px);
}

.card-top {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 18px;
}

.avatar {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: #eff6ff;
  color: #2563eb;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  font-weight: 700;
  flex-shrink: 0;
}

.card-info {
  flex: 1;
}

.card-info h2 {
  font-size: 15px;
  color: #111827;
  font-weight: 600;
  margin-bottom: 3px;
}

.drive-name {
  color: #6b7280;
  font-size: 13px;
}

.card-details {
  display: flex;
  gap: 10px;
  margin-bottom: 18px;
}

.detail-item {
  flex: 1;
  background: #f9fafb;
  padding: 12px;
  border-radius: 10px;
}

.detail-label {
  color: #6b7280;
  font-size: 12px;
  margin-bottom: 4px;
}

.detail-item h4 {
  color: #111827;
  font-size: 13px;
  font-weight: 600;
}

.view-btn {
  width: 100%;
  border: none;
  background: #2563eb;
  color: white;
  padding: 11px;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.view-btn:hover {
  background: #1d4ed8;
}

.status-badge {
  padding: 5px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}

.status-pending  { background: #fef9c3; color: #ca8a04; }
.status-selected { background: #dcfce7; color: #16a34a; }
.status-rejected { background: #fee2e2; color: #dc2626; }

.empty {
  text-align: center;
  color: #9ca3af;
  font-size: 15px;
  padding: 60px 0;
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
  width: 480px;
  max-width: 90%;
  padding: 28px;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
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

.detail-label { color: #6b7280; }

.detail-value {
  color: #111827;
  font-weight: 600;
  text-align: right;
  max-width: 60%;
  word-break: break-word;
}

.modal-actions {
  display: flex;
  gap: 10px;
}

.btn-select {
  flex: 1;
  padding: 11px;
  background: #dcfce7;
  color: #16a34a;
  border: none;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-select:hover { background: #bbf7d0; }

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

.btn-reject:hover { background: #fecaca; }

</style>