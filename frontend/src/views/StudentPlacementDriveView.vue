<template>
  <div>

    <div class="topbar">
      <div>
        <h1>Placement Drives</h1>
        <p>All available placement drives</p>
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
            <th>Job Title</th>
            <th>Last Date</th>
            <th>Salary</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(drive, index) in filteredDrives" :key="drive.id">
            <td>{{ index + 1 }}</td>
            <td>{{ drive.company }}</td>
            <td>{{ drive.job_title }}</td>
            <td>{{ drive.last_date }}</td>
            <td>{{ drive.salary }}</td>
            <td>
              <span :class="
                drive.status === 'Upcoming'  ? 'badge-upcoming'  :
                drive.status === 'Ongoing'   ? 'badge-ongoing'   :
                'badge-completed'
              ">
                {{ drive.status }}
              </span>
            </td>
            <td>
              <div class="actions">
                <button class="btn-view"  @click="viewDetail(drive)">View Details</button>
                <button class="btn-apply">Apply</button>
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
          <h3>Drive Details</h3>
          <button class="btn-close" @click="selectedDrive = null">✕</button>
        </div>

        <div class="detail-top">
          <div class="avatar-lg">{{ selectedDrive.company.charAt(0) }}</div>
          <div>
            <h4>{{ selectedDrive.company }}</h4>
            <p>{{ selectedDrive.job_title }} · {{ selectedDrive.salary }}</p>
          </div>
          <span :class="
            selectedDrive.status === 'Upcoming'  ? 'badge-upcoming'  :
            selectedDrive.status === 'Ongoing'   ? 'badge-ongoing'   :
            'badge-completed'
          ">{{ selectedDrive.status }}</span>
        </div>

        <div class="detail-rows">
          <div class="detail-row">
            <span class="detail-label">Company</span>
            <span class="detail-value">{{ selectedDrive.company }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Job Title</span>
            <span class="detail-value">{{ selectedDrive.job_title }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Salary</span>
            <span class="detail-value">{{ selectedDrive.salary }}</span>
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
            <span class="detail-label">Job Description</span>
            <span class="detail-value">{{ selectedDrive.job_description }}</span>
          </div>
        </div>

        <div class="modal-footer">
          <button class="btn-close-modal" @click="selectedDrive = null">Close</button>
          <button class="btn-apply-modal">Apply Now</button>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "StudentPlacementDrivesView",

  data() {
    return {
      search: "",
      selectedDrive: null,
      drives: [
        { id: 1, company: "Google",    job_title: "Software Engineer",    start_date: "20 May 2026", last_date: "25 May 2026", salary: "45 LPA", skills_required: "DSA, System Design, Python",    job_description: "SWE role at Google India.",        status: "Upcoming"  },
        { id: 2, company: "Microsoft", job_title: "SDE-1",                start_date: "22 May 2026", last_date: "28 May 2026", salary: "40 LPA", skills_required: "C++, Java, System Design",      job_description: "Software Dev Engineer role.",       status: "Upcoming"  },
        { id: 3, company: "Amazon",    job_title: "Backend Developer",    start_date: "15 May 2026", last_date: "20 May 2026", salary: "35 LPA", skills_required: "Node.js, AWS, Databases",       job_description: "Backend dev at Amazon India.",      status: "Ongoing"   },
        { id: 4, company: "Flipkart",  job_title: "Frontend Developer",   start_date: "25 May 2026", last_date: "30 May 2026", salary: "28 LPA", skills_required: "React, Vue.js, CSS",            job_description: "Frontend dev at Flipkart.",         status: "Upcoming"  },
        { id: 5, company: "Zomato",    job_title: "Full Stack Developer", start_date: "12 May 2026", last_date: "18 May 2026", salary: "18 LPA", skills_required: "React, Node.js, MongoDB",       job_description: "Full stack role at Zomato.",        status: "Ongoing"   },
        { id: 6, company: "Infosys",   job_title: "Systems Engineer",     start_date: "10 May 2026", last_date: "15 May 2026", salary: "8 LPA",  skills_required: "Java, SQL, Networking",          job_description: "Systems Engineer program.",         status: "Completed" },
        { id: 7, company: "TCS",       job_title: "Developer",            start_date: "05 May 2026", last_date: "10 May 2026", salary: "7 LPA",  skills_required: "Java, Python, SQL",             job_description: "TCS NextStep developer role.",      status: "Completed" },
        { id: 8, company: "Wipro",     job_title: "Junior Developer",     start_date: "18 May 2026", last_date: "22 May 2026", salary: "6 LPA",  skills_required: "Java, C++, Communication",      job_description: "Junior dev at Wipro Technologies.", status: "Upcoming"  },
      ]
    }
  },

  computed: {
    filteredDrives() {
      const q = this.search.toLowerCase()
      return this.drives.filter(drive =>
        drive.company.toLowerCase().includes(q) ||
        drive.job_title.toLowerCase().includes(q)
      )
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
  margin-bottom: 5px;
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

.btn-apply {
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

.btn-apply:hover {
  background: #bbf7d0;
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

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
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

.btn-apply-modal {
  background: #dcfce7;
  color: #16a34a;
  border: none;
  padding: 9px 18px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-apply-modal:hover {
  background: #bbf7d0;
}

</style>