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

    <div class="table-box">
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
            <td>{{ app.package }}</td>
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

    <div v-if="selectedApp" class="modal-overlay" @click.self="selectedApp = null">
      <div class="modal">

        <div class="modal-header">
          <h3>Application Detail</h3>
          <button class="btn-close" @click="selectedApp = null">✕</button>
        </div>

        <div class="detail-top">
          <div class="avatar-lg">{{ selectedApp.student_name.charAt(0) }}</div>
          <div>
            <h4>{{ selectedApp.student_name }}</h4>
            <p>{{ selectedApp.company }} · {{ selectedApp.drive }}</p>
          </div>
          <span :class="getStatusClass(selectedApp.status)">{{ selectedApp.status }}</span>
        </div>

        <div class="detail-rows">
          <div class="detail-row">
            <span class="detail-label">Student Name</span>
            <span class="detail-value">{{ selectedApp.student_name }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Branch</span>
            <span class="detail-value">{{ selectedApp.branch }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">CGPA</span>
            <span class="detail-value">{{ selectedApp.cgpa }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Email</span>
            <span class="detail-value">{{ selectedApp.email }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Company</span>
            <span class="detail-value">{{ selectedApp.company }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Role</span>
            <span class="detail-value">{{ selectedApp.drive }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Package</span>
            <span class="detail-value">{{ selectedApp.package }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Applied On</span>
            <span class="detail-value">{{ selectedApp.date }}</span>
          </div>
          <div class="detail-row">
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
</template>

<script>
export default {
  name: "StudentApplicationsView",

  data() {
    return {
      search: "",
      selectedApp: null,
      applications: [
        { id: 1, company: "Google",    drive: "Software Engineer Hiring", date: "20 May 2026", package: "45 LPA", status: "Applied",     student_name: "Rahul Sharma", branch: "CSE", cgpa: "8.5", email: "rahul@college.edu", resume: "#" },
        { id: 2, company: "Microsoft", drive: "SDE-1 Recruitment",        date: "18 May 2026", package: "40 LPA", status: "Shortlisted", student_name: "Rahul Sharma", branch: "CSE", cgpa: "8.5", email: "rahul@college.edu", resume: "#" },
        { id: 3, company: "Amazon",    drive: "Backend Developer Drive",  date: "15 May 2026", package: "35 LPA", status: "Rejected",    student_name: "Rahul Sharma", branch: "CSE", cgpa: "8.5", email: "rahul@college.edu", resume: "#" },
        { id: 4, company: "Flipkart",  drive: "Frontend Hiring",          date: "12 May 2026", package: "28 LPA", status: "Selected",    student_name: "Rahul Sharma", branch: "CSE", cgpa: "8.5", email: "rahul@college.edu", resume: "#" },
        { id: 5, company: "Zomato",    drive: "Full Stack Developer",     date: "22 May 2026", package: "18 LPA", status: "Applied",     student_name: "Rahul Sharma", branch: "CSE", cgpa: "8.5", email: "rahul@college.edu", resume: "#" },
      ]
    }
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
    getStatusClass(status) {
      if (status === 'Selected')    return 'badge-selected'
      if (status === 'Shortlisted') return 'badge-shortlisted'
      if (status === 'Rejected')    return 'badge-rejected'
      return 'badge-applied'
    },

    viewDetail(app) {
      this.selectedApp = app
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