<template>
  <div class="drives-page">

    <div class="topbar">
      <div>
        <h1>Placement Drives</h1>
        <p>All your posted placement drives</p>
      </div>
      <input
        v-model="search"
        type="text"
        placeholder="Search by role..."
        class="search-input"
      />
    </div>

    <div class="drives-grid">
      <div
        class="drive-card"
        v-for="drive in filteredDrives"
        :key="drive.id"
      >
        <div class="card-top">
          <div class="avatar">{{ drive.role.charAt(0) }}</div>
          <div class="card-info">
            <h3>{{ drive.role }}</h3>
            <p>{{ drive.package }}</p>
          </div>
          <span :class="
            drive.status === 'Upcoming'  ? 'badge-upcoming'  :
            drive.status === 'Ongoing'   ? 'badge-ongoing'   :
            'badge-completed'
          ">{{ drive.status }}</span>
        </div>

        <div class="card-details">
          <div class="detail-item">
            <p class="detail-label">Start Date</p>
            <h4>{{ drive.start_date }}</h4>
          </div>
          <div class="detail-item">
            <p class="detail-label">Last Date</p>
            <h4>{{ drive.last_date }}</h4>
          </div>
        </div>

        <button class="view-btn" @click="viewDetail(drive)">View Detail</button>

      </div>
    </div>

    <div v-if="filteredDrives.length === 0" class="empty">
      No drives found
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
            <span class="detail-label">Status</span>
            <span :class="
              selectedDrive.status === 'Upcoming'  ? 'badge-upcoming'  :
              selectedDrive.status === 'Ongoing'   ? 'badge-ongoing'   :
              'badge-completed'
            ">{{ selectedDrive.status }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Description</span>
            <span class="detail-value">{{ selectedDrive.description }}</span>
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

.drives-page {
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

.drives-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 18px;
}

.drive-card {
  background: white;
  border-radius: 18px;
  padding: 20px;
  border: 1px solid #f1f5f9;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  gap: 16px;
  transition: 0.2s;
}

.drive-card:hover {
  transform: translateY(-3px);
}

.card-top {
  display: flex;
  align-items: center;
  gap: 12px;
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

.card-info h3 {
  font-size: 15px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 3px;
}

.card-info p {
  font-size: 13px;
  color: #6b7280;
}

.card-details {
  display: flex;
  gap: 10px;
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

.badge-upcoming  { background: #dbeafe; color: #2563eb; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; white-space: nowrap; }
.badge-ongoing   { background: #fef9c3; color: #ca8a04; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; white-space: nowrap; }
.badge-completed { background: #f3f4f6; color: #6b7280; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; white-space: nowrap; }

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

.detail-label { color: #6b7280; }

.detail-value {
  color: #111827;
  font-weight: 600;
  text-align: right;
  max-width: 60%;
  word-break: break-word;
}

</style>