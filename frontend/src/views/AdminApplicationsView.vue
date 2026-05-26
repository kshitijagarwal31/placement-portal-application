<template>
  <div>

    <div class="topbar">
      <div>
        <h1>Applications</h1>
        <p>All student applications</p>
      </div>
      <input
        v-model="search"
        class="search-input"
        type="text"
        placeholder="Search by student, company or status..."
      />
    </div>

    <div class="table-box">
      <table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Student</th>
            <th>Company</th>
            <th>Role</th>
            <th>Applied On</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(application, index) in filteredApplications" :key="application.id">
            <td>{{ index + 1 }}</td>
            <td>{{ application.student }}</td>
            <td>{{ application.company }}</td>
            <td>{{ application.role }}</td>
            <td>{{ application.appliedOn }}</td>
            <td>
              <span :class="
                application.status === 'Selected' ? 'badge-selected' :
                application.status === 'Pending'  ? 'badge-pending'  :
                'badge-rejected'
              ">
                {{ application.status }}
              </span>
            </td>
            <td>
              <button class="btn-view" @click="viewDetail(application)">View</button>
            </td>
          </tr>
        </tbody>
      </table>

      <div v-if="filteredApplications.length === 0" class="empty">
        No applications found
      </div>
    </div>

    <div v-if="selectedApplication" class="modal-overlay" @click.self="selectedApplication = null">
      <div class="modal">

        <div class="modal-header">
          <h3>Application Detail</h3>
          <button class="btn-close" @click="selectedApplication = null">✕</button>
        </div>

        <div class="detail-top">
          <div class="avatar-lg">{{ selectedApplication.student.charAt(0) }}</div>
          <div>
            <h4>{{ selectedApplication.student }}</h4>
            <p>{{ selectedApplication.company }} · {{ selectedApplication.role }}</p>
          </div>
          <span :class="
            selectedApplication.status === 'Selected' ? 'badge-selected' :
            selectedApplication.status === 'Pending'  ? 'badge-pending'  :
            'badge-rejected'
          ">{{ selectedApplication.status }}</span>
        </div>

        <div class="detail-rows">
          <div class="detail-row">
            <span class="detail-label">Student Name</span>
            <span class="detail-value">{{ selectedApplication.student }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Branch</span>
            <span class="detail-value">{{ selectedApplication.branch }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">CGPA</span>
            <span class="detail-value">{{ selectedApplication.cgpa }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Email</span>
            <span class="detail-value">{{ selectedApplication.email }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Company</span>
            <span class="detail-value">{{ selectedApplication.company }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Role</span>
            <span class="detail-value">{{ selectedApplication.role }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Package</span>
            <span class="detail-value">{{ selectedApplication.package }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Applied On</span>
            <span class="detail-value">{{ selectedApplication.appliedOn }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Resume</span>
            <a :href="selectedApplication.resume" target="_blank" class="website-link">📄 View Resume</a>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "AdminApplicationsView",

  data() {
    return {
      search: "",
      selectedApplication: null,
      applications: [
        { id: 1, student: "Rahul Sharma",  branch: "CSE", cgpa: "8.5", email: "rahul@college.edu",  company: "Google",    role: "Software Engineer",    package: "45 LPA", appliedOn: "10 May 2026", resume: "#", status: "Selected" },
        { id: 2, student: "Priya Singh",   branch: "IT",  cgpa: "7.9", email: "priya@college.edu",  company: "Microsoft", role: "SDE-1",                package: "40 LPA", appliedOn: "11 May 2026", resume: "#", status: "Pending"  },
        { id: 3, student: "Amit Kumar",    branch: "CSE", cgpa: "8.1", email: "amit@college.edu",   company: "Amazon",    role: "Backend Developer",    package: "35 LPA", appliedOn: "12 May 2026", resume: "#", status: "Rejected" },
        { id: 4, student: "Sneha Verma",   branch: "ECE", cgpa: "7.2", email: "sneha@college.edu",  company: "Flipkart",  role: "Frontend Developer",   package: "28 LPA", appliedOn: "13 May 2026", resume: "#", status: "Selected" },
        { id: 5, student: "Rohan Gupta",   branch: "CSE", cgpa: "7.5", email: "rohan@college.edu",  company: "Zomato",    role: "Full Stack Developer", package: "18 LPA", appliedOn: "14 May 2026", resume: "#", status: "Pending"  },
        { id: 6, student: "Pooja Yadav",   branch: "IT",  cgpa: "8.0", email: "pooja@college.edu",  company: "Infosys",   role: "Systems Engineer",     package: "8 LPA",  appliedOn: "15 May 2026", resume: "#", status: "Selected" },
        { id: 7, student: "Vikram Patel",  branch: "CSE", cgpa: "6.8", email: "vikram@college.edu", company: "TCS",       role: "Developer",            package: "7 LPA",  appliedOn: "16 May 2026", resume: "#", status: "Rejected" },
        { id: 8, student: "Anjali Mishra", branch: "ECE", cgpa: "7.1", email: "anjali@college.edu", company: "Wipro",     role: "Junior Developer",     package: "6 LPA",  appliedOn: "17 May 2026", resume: "#", status: "Pending"  },
      ]
    }
  },

  computed: {
    filteredApplications() {
      const q = this.search.toLowerCase()
      return this.applications.filter(a =>
        a.student.toLowerCase().includes(q) ||
        a.company.toLowerCase().includes(q) ||
        a.status.toLowerCase().includes(q)
      )
    }
  },

  methods: {
    viewDetail(application) {
      this.selectedApplication = application
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

.badge-selected {
  background: #dcfce7;
  color: #16a34a;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.badge-pending {
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

.website-link {
  color: #2563eb;
  font-weight: 600;
  font-size: 14px;
  text-decoration: none;
}

.website-link:hover {
  text-decoration: underline;
}

</style>