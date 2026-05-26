<template>
  <div>

    <div class="topbar">
      <div>
        <h1>Placement Drives</h1>
        <p>All your posted placement drives</p>
      </div>
      <input
        v-model="search"
        class="search-input"
        type="text"
        placeholder="Search by role or status..."
      />
    </div>

    <div class="table-box">
      <table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Role</th>
            <th>Start Date</th>
            <th>Last Date</th>
            <th>Package</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(drive, index) in filteredDrives" :key="drive.id">
            <td>{{ index + 1 }}</td>
            <td>{{ drive.role }}</td>
            <td>{{ drive.start_date }}</td>
            <td>{{ drive.last_date }}</td>
            <td>{{ drive.package }}</td>
            <td>
              <span :class="
                drive.status === 'Upcoming'  ? 'badge-upcoming'  :
                drive.status === 'Ongoing'   ? 'badge-ongoing'   :
                'badge-completed'
              ">{{ drive.status }}</span>
            </td>
            <td>
              <div class="actions">
                <button class="btn-view" @click="viewDetail(drive)">View Detail</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <div v-if="filteredDrives.length === 0" class="empty">
        No drives found
      </div>
    </div>

    <div v-if="selectedDrive" class="modal-overlay" @click.self="selectedDrive = null">
      <div class="modal">

        <div class="modal-header">
          <h3>Drive Detail</h3>
          <button class="btn-close" @click="selectedDrive = null">✕</button>
        </div>

        <div class="detail-rows">
          <div class="detail-row">
            <span class="detail-label">Role</span>
            <span class="detail-value">{{ selectedDrive.role }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Package</span>
            <span class="detail-value">{{ selectedDrive.package }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Start Date</span>
            <span class="detail-value">{{ selectedDrive.start_date }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Last Date</span>
            <span class="detail-value">{{ selectedDrive.last_date }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Skills Required</span>
            <span class="detail-value">{{ selectedDrive.skills_required }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Description</span>
            <span class="detail-value">{{ selectedDrive.description }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Status</span>
            <span :class="
              selectedDrive.status === 'Upcoming'  ? 'badge-upcoming'  :
              selectedDrive.status === 'Ongoing'   ? 'badge-ongoing'   :
              'badge-completed'
            ">{{ selectedDrive.status }}</span>
          </div>
        </div>

        <div class="app-section">
          <h4 class="app-section-title">
            Applications
            <span class="app-count">{{ driveApplications.length }}</span>
          </h4>

          <div v-if="driveApplications.length === 0" class="app-empty">
            No applications yet
          </div>

          <div class="app-table-box" v-else>
            <table class="app-table">
              <thead>
                <tr>
                  <th>S.No</th>
                  <th>Student</th>
                  <th>Branch</th>
                  <th>CGPA</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(app, index) in driveApplications" :key="app.id">
                  <td>{{ index + 1 }}</td>
                  <td>{{ app.student }}</td>
                  <td>{{ app.branch }}</td>
                  <td>{{ app.cgpa }}</td>
                  <td>
                    <span :class="[
                      'status-badge',
                      app.status === 'Pending'  ? 'status-pending'  :
                      app.status === 'Selected' ? 'status-selected' :
                      'status-rejected'
                    ]">{{ app.status }}</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

        </div>

      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "CompanyDrivesView",

  data() {
    return {
      search: "",
      selectedDrive: null,
      drives: [
        { id: 1, role: "Software Engineer",    package: "45 LPA", start_date: "25 May 2026", last_date: "30 May 2026", skills_required: "Python, DSA",     status: "Upcoming",  description: "Looking for strong problem solvers." },
        { id: 2, role: "Frontend Developer",   package: "30 LPA", start_date: "20 May 2026", last_date: "28 May 2026", skills_required: "React, CSS",       status: "Ongoing",   description: "Build beautiful user interfaces."    },
        { id: 3, role: "Backend Developer",    package: "35 LPA", start_date: "22 May 2026", last_date: "29 May 2026", skills_required: "Node.js, MongoDB", status: "Upcoming",  description: "Work on scalable backend systems."   },
        { id: 4, role: "Full Stack Developer", package: "40 LPA", start_date: "10 May 2026", last_date: "18 May 2026", skills_required: "Vue, Node, MySQL", status: "Completed", description: "End to end product development."     },
        { id: 5, role: "Data Analyst",         package: "20 LPA", start_date: "08 May 2026", last_date: "15 May 2026", skills_required: "Python, SQL",      status: "Completed", description: "Analyze data and build reports."     },
      ],
      applications: [
        { id: 1, drive: "Software Engineer",    student: "Rahul Sharma", branch: "CSE", cgpa: "8.9", status: "Pending"  },
        { id: 2, drive: "Software Engineer",    student: "Sneha Verma",  branch: "CSE", cgpa: "9.2", status: "Selected" },
        { id: 3, drive: "Frontend Developer",   student: "Priya Singh",  branch: "ECE", cgpa: "7.5", status: "Selected" },
        { id: 4, drive: "Frontend Developer",   student: "Pooja Yadav",  branch: "CSE", cgpa: "8.4", status: "Pending"  },
        { id: 5, drive: "Backend Developer",    student: "Amit Kumar",   branch: "ME",  cgpa: "8.1", status: "Rejected" },
        { id: 6, drive: "Full Stack Developer", student: "Rohan Gupta",  branch: "IT",  cgpa: "7.8", status: "Pending"  },
      ]
    }
  },

  computed: {
    filteredDrives() {
      const q = this.search.toLowerCase()
      return this.drives.filter(d =>
        d.role.toLowerCase().includes(q) ||
        d.status.toLowerCase().includes(q)
      )
    },
    driveApplications() {
      if (!this.selectedDrive) return []
      return this.applications.filter(a => a.drive === this.selectedDrive.role)
    }
  },

  methods: {
    viewDetail(drive) {
      this.selectedDrive = drive
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

.badge-upcoming,
.badge-ongoing,
.badge-completed {
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.badge-upcoming { 
  background: #dbeafe;
  color: #2563eb;
  }

.badge-ongoing {
  background: #fef9c3;
  color: #ca8a04; 
  }

.badge-completed { 
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
  margin-bottom: 24px;
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

.detail-rows {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 28px;
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

.app-section {
  margin-top: 4px;
}

.app-section-title {
  font-size: 15px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.app-count {
  background: #eff6ff;
  color: #2563eb;
  padding: 2px 10px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.app-empty {
  text-align: center;
  color: #9ca3af;
  font-size: 14px;
  padding: 20px 0;
}

.app-table-box {
  border-radius: 12px;
  border: 1px solid #e5e7eb;
  overflow: hidden;
}

.app-table {
  width: 100%;
  border-collapse: collapse;
}

.app-table thead {
  background: #f9fafb;
}

.app-table th {
  padding: 12px 16px;
  text-align: left;
  font-size: 13px;
  color: #6b7280;
  font-weight: 600;
  border-bottom: 1px solid #e5e7eb;
}

.app-table td {
  padding: 12px 16px;
  font-size: 14px;
  color: #111827;
  border-bottom: 1px solid #f3f4f6;
  font-weight: 500;
}

.app-table tr:last-child td {
  border-bottom: none;
}

.app-table tr:hover td {
  background: #f9fafb;
}

.status-badge {
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}

.status-pending  { 
  background: #fef9c3; 
  color: #ca8a04; 
}

.status-selected { 
  background: #dcfce7; 
  color: #16a34a;
}

.status-rejected { 
  background: #fee2e2; 
  color: #dc2626; 
}

</style>