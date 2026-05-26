<template>
  <div>

    <div class="topbar">
      <div>
        <h1>Placement Drives</h1>
        <p>All placement drives</p>
      </div>
      <input
        v-model="search"
        class="search-input"
        type="text"
        placeholder="Search by company, role or status..."
      />
    </div>

    <div class="table-box">
      <table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Company</th>
            <th>Role</th>
            <th>Date</th>
            <th>Package</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(drive, index) in filteredDrives" :key="drive.id">
            <td>{{ index + 1 }}</td>
            <td>{{ drive.company }}</td>
            <td>{{ drive.role }}</td>
            <td>{{ drive.date }}</td>
            <td>{{ drive.package }}</td>
            <td>
              <span :class="
                drive.status === 'Pending'   ? 'badge-pending'   :
                drive.status === 'Active'    ? 'badge-active'    :
                drive.status === 'Rejected'  ? 'badge-rejected'  :
                drive.status === 'Upcoming'  ? 'badge-upcoming'  :
                drive.status === 'Ongoing'   ? 'badge-ongoing'   :
                'badge-completed'
              ">
                {{ drive.status }}
              </span>
            </td>
            <td>
              <div class="actions">

                <template v-if="drive.status === 'Pending'">
                  <button class="btn-approve" @click="approveDrive(drive)">Approve</button>
                  <button class="btn-reject"  @click="rejectDrive(drive)">Reject</button>
                </template>

                <template v-if="drive.status === 'Active' || drive.status === 'Upcoming' || drive.status === 'Ongoing' || drive.status === 'Completed'">
                  <button class="btn-view" @click="viewDetail(drive)">View Detail</button>
                </template>

                <template v-if="drive.status === 'Rejected'">
                  <span class="text-rejected">—</span>
                </template>

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

        <div class="detail-top">
          <div class="avatar-lg">{{ selectedDrive.company.charAt(0) }}</div>
          <div>
            <h4>{{ selectedDrive.company }}</h4>
            <p>{{ selectedDrive.role }} · {{ selectedDrive.package }}</p>
          </div>
          <span :class="
            selectedDrive.status === 'Upcoming'  ? 'badge-upcoming'  :
            selectedDrive.status === 'Ongoing'   ? 'badge-ongoing'   :
            selectedDrive.status === 'Completed' ? 'badge-completed' :
            selectedDrive.status === 'Active'    ? 'badge-active'    :
            selectedDrive.status === 'Pending'   ? 'badge-pending'   :
            'badge-rejected'
          ">{{ selectedDrive.status }}</span>
        </div>

        <div class="detail-rows">
          <div class="detail-row">
            <span class="detail-label">Company</span>
            <span class="detail-value">{{ selectedDrive.company }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Role</span>
            <span class="detail-value">{{ selectedDrive.role }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Package</span>
            <span class="detail-value">{{ selectedDrive.package }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Drive Date</span>
            <span class="detail-value">{{ selectedDrive.date }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Eligibility</span>
            <span class="detail-value">{{ selectedDrive.eligibility }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Location</span>
            <span class="detail-value">{{ selectedDrive.location }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Description</span>
            <span class="detail-value">{{ selectedDrive.description }}</span>
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
                  <th>Student Name</th>
                  <th>Branch</th>
                  <th>CGPA</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(app, index) in driveApplications" :key="app.id">
                  <td>{{ index + 1 }}</td>
                  <td>{{ app.student_name }}</td>
                  <td>{{ app.branch }}</td>
                  <td>{{ app.cgpa }}</td>
                  <td>
                    <span :class="
                      app.status === 'Applied'   ? 'status-applied'   :
                      app.status === 'Shortlisted' ? 'status-shortlisted' :
                      app.status === 'Selected'  ? 'status-selected'  :
                      'status-rejected'
                    ">{{ app.status }}</span>
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
  name: "AdminPlacementDrivesView",

  data() {
    return {
      search: "",
      selectedDrive: null,

      drives: [
        { id: 1, company: "Google",    role: "Software Engineer",    date: "25 May 2026", package: "45 LPA", status: "Pending",   eligibility: "8.0+ CGPA, CSE/IT",       location: "Bangalore",  description: "SWE role at Google India." },
        { id: 2, company: "Microsoft", role: "SDE-1",                date: "28 May 2026", package: "40 LPA", status: "Pending",   eligibility: "7.5+ CGPA, CSE/IT/ECE",   location: "Hyderabad",  description: "Software Dev Engineer role." },
        { id: 3, company: "Amazon",    role: "Backend Developer",    date: "20 May 2026", package: "35 LPA", status: "Ongoing",   eligibility: "7.0+ CGPA, All branches",  location: "Bangalore",  description: "Backend dev at Amazon India." },
        { id: 4, company: "Infosys",   role: "Systems Engineer",     date: "15 May 2026", package: "8 LPA",  status: "Completed", eligibility: "6.5+ CGPA, All branches",  location: "Pune",       description: "Systems Engineer program." },
        { id: 5, company: "TCS",       role: "Developer",            date: "10 May 2026", package: "7 LPA",  status: "Completed", eligibility: "6.0+ CGPA, All branches",  location: "Mumbai",     description: "TCS NextStep developer role." },
        { id: 6, company: "Flipkart",  role: "Frontend Developer",   date: "30 May 2026", package: "28 LPA", status: "Upcoming",  eligibility: "7.5+ CGPA, CSE/IT",       location: "Bangalore",  description: "Frontend dev at Flipkart." },
        { id: 7, company: "Zomato",    role: "Full Stack Developer", date: "18 May 2026", package: "18 LPA", status: "Pending",   eligibility: "7.0+ CGPA, CSE/IT/ECE",   location: "Gurgaon",    description: "Full stack role at Zomato." },
        { id: 8, company: "Wipro",     role: "Junior Developer",     date: "12 May 2026", package: "6 LPA",  status: "Completed", eligibility: "6.0+ CGPA, All branches",  location: "Delhi",      description: "Junior dev at Wipro Technologies." },
      ],

      applications: [
        { id: 1, drive_id: 3, student_name: "Rahul Sharma",   branch: "CSE",  cgpa: "8.5", status: "Shortlisted" },
        { id: 2, drive_id: 3, student_name: "Priya Singh",    branch: "IT",   cgpa: "7.9", status: "Applied"     },
        { id: 3, drive_id: 3, student_name: "Amit Kumar",     branch: "CSE",  cgpa: "8.1", status: "Selected"    },
        { id: 4, drive_id: 4, student_name: "Sneha Verma",    branch: "ECE",  cgpa: "7.2", status: "Selected"    },
        { id: 5, drive_id: 4, student_name: "Rohit Gupta",    branch: "CSE",  cgpa: "6.8", status: "Rejected"    },
        { id: 6, drive_id: 5, student_name: "Anjali Mishra",  branch: "IT",   cgpa: "7.5", status: "Selected"    },
        { id: 7, drive_id: 6, student_name: "Vikas Yadav",    branch: "CSE",  cgpa: "8.0", status: "Applied"     },
        { id: 8, drive_id: 8, student_name: "Pooja Tiwari",   branch: "CSE",  cgpa: "7.1", status: "Selected"    },
        { id: 9, drive_id: 8, student_name: "Karan Joshi",    branch: "IT",   cgpa: "6.5", status: "Rejected"    },
      ]
    }
  },

  computed: {
    filteredDrives() {
      const q = this.search.toLowerCase()
      return this.drives.filter(d =>
        d.company.toLowerCase().includes(q) ||
        d.role.toLowerCase().includes(q)    ||
        d.status.toLowerCase().includes(q)
      )
    },
    driveApplications() {
      if (!this.selectedDrive) return []
      return this.applications.filter(a => a.drive_id === this.selectedDrive.id)
    }
  },

  methods: {
    viewDetail(drive) {
      this.selectedDrive = drive
    },
    approveDrive(drive) {
      drive.status = 'Active'
    },
    rejectDrive(drive) {
      drive.status = 'Rejected'
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

.actions {
  display: flex;
  gap: 10px;
  align-items: center;
}

.btn-approve {
  background: #dcfce7;
  color: #16a34a;
  border: none;
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-approve:hover {
  background: #bbf7d0;
}

.btn-reject {
  background: #fee2e2;
  color: #dc2626;
  border: none;
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-reject:hover {
  background: #fecaca;
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

.text-rejected {
  color: #9ca3af;
  font-size: 15px;
}

.badge-pending {
  background: #fef9c3;
  color: #ca8a04;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.badge-active {
  background: #dcfce7;
  color: #16a34a;
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

.badge-upcoming {
  background: #dbeafe;
  color: #2563eb;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.badge-ongoing {
  background: #fef9c3;
  color: #ca8a04;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.badge-completed {
  background: #dcfce7;
  color: #16a34a;
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

.status-applied {
  background: #dbeafe;
  color: #2563eb;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}

.status-shortlisted {
  background: #fef9c3;
  color: #ca8a04;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}

.status-selected {
  background: #dcfce7;
  color: #16a34a;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}

.status-rejected {
  background: #fee2e2;
  color: #dc2626;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}

</style>