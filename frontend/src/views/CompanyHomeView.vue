<template>
  <div>

    <div class="topbar">
      <h1>Company Dashboard</h1>
    </div>

    <div class="cards">
      <div class="card">
        <h2>{{ totalJobs }}</h2>
        <p>Jobs Posted</p>
      </div>
      <div class="card">
        <h2>{{ totalApplicants }}</h2>
        <p>Total Applicants</p>
      </div>
      <div class="card">
        <h2>{{ totalSelected }}</h2>
        <p>Selected</p>
      </div>
      <div class="card">
        <h2>{{ totalDrives }}</h2>
        <p>Placement Drives</p>
      </div>
    </div>

    <div class="requests-grid">

      <div class="section-box">
        <div class="section-header">
          <h3>Recent Applicants</h3>
        </div>

        <div v-if="applicants.length === 0" class="empty">
          No applicants yet
        </div>

        <div
          v-for="app in applicants.slice(0, 5)"
          :key="app.id"
          class="request-item"
        >
          <div class="request-left">
            <div class="avatar">{{ app.name.charAt(0) }}</div>
            <div>
              <p class="request-name">{{ app.name }}</p>
              <p class="request-sub">{{ app.role }} · {{ app.branch }}</p>
            </div>
          </div>
          <span :class="
            app.status === 'Selected' ? 'badge-selected' :
            app.status === 'Pending'  ? 'badge-pending'  :
            'badge-rejected'
          ">{{ app.status }}</span>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header">
          <h3>Active Drives</h3>
        </div>

        <div v-if="drives.length === 0" class="empty">
          No active drives
        </div>

        <div
          v-for="drive in drives.slice(0, 5)"
          :key="drive.id"
          class="request-item"
        >
          <div class="request-left">
            <div class="avatar">{{ drive.role.charAt(0) }}</div>
            <div>
              <p class="request-name">{{ drive.role }}</p>
              <p class="request-sub">{{ drive.date }} · {{ drive.package }}</p>
            </div>
          </div>
          <span :class="
            drive.status === 'Active'   ? 'badge-active'   :
            drive.status === 'Pending'  ? 'badge-pending'  :
            'badge-completed'
          ">{{ drive.status }}</span>
        </div>
      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: "CompanyHomeView",

  data() {
    return {
      applicants: [
        { id: 1, name: "Rahul Sharma",  role: "Software Engineer",   branch: "CSE", status: "Selected" },
        { id: 2, name: "Priya Singh",   role: "Frontend Developer",  branch: "ECE", status: "Pending"  },
        { id: 3, name: "Amit Kumar",    role: "Backend Developer",   branch: "ME",  status: "Rejected" },
        { id: 4, name: "Sneha Verma",   role: "Software Engineer",   branch: "CSE", status: "Selected" },
        { id: 5, name: "Rohan Gupta",   role: "Full Stack Developer", branch: "IT",  status: "Pending"  },
      ],
      drives: [
        { id: 1, role: "Software Engineer",    date: "25 May 2026", package: "45 LPA", status: "Active"    },
        { id: 2, role: "Frontend Developer",   date: "28 May 2026", package: "30 LPA", status: "Pending"   },
        { id: 3, role: "Backend Developer",    date: "30 May 2026", package: "35 LPA", status: "Active"    },
        { id: 4, role: "Full Stack Developer",  date: "02 Jun 2026", package: "40 LPA", status: "Completed" },
      ]
    }
  },

  computed: {
    totalJobs()       { return this.drives.length },
    totalApplicants() { return this.applicants.length },
    totalSelected()   { return this.applicants.filter(a => a.status === 'Selected').length },
    totalDrives()     { return this.drives.filter(d => d.status === 'Active').length }
  }
}
</script>

<style scoped>

.topbar {
  margin-bottom: 30px;
}

.topbar h1 {
  font-size: 34px;
  color: #111827;
}

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.card {
  background: white;
  padding: 24px;
  border-radius: 18px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.card h2 {
  font-size: 30px;
  color: #2563eb;
  margin-bottom: 8px;
  font-weight: 700;
}

.card p {
  color: #6b7280;
  font-size: 14px;
}

.requests-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.section-box {
  background: white;
  border-radius: 18px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  padding: 24px;
}

.section-header {
  margin-bottom: 20px;
}

.section-header h3 {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
}

.request-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 0;
  border-bottom: 1px solid #f3f4f6;
}

.request-item:last-of-type {
  border-bottom: none;
}

.request-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.avatar {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: #eff6ff;
  color: #2563eb;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 15px;
  font-weight: 700;
  flex-shrink: 0;
}

.request-name {
  font-size: 14px;
  font-weight: 600;
  color: #111827;
}

.request-sub {
  font-size: 13px;
  color: #6b7280;
  margin-top: 2px;
}

.badge-selected {
  background: #dcfce7;
  color: #16a34a;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 20px;
  white-space: nowrap;
}

.badge-pending {
  background: #fef9c3;
  color: #ca8a04;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 20px;
  white-space: nowrap;
}

.badge-rejected {
  background: #fee2e2;
  color: #dc2626;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 20px;
  white-space: nowrap;
}

.badge-active {
  background: #dcfce7;
  color: #16a34a;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 20px;
  white-space: nowrap;
}

.badge-completed {
  background: #f3f4f6;
  color: #6b7280;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 20px;
  white-space: nowrap;
}

.empty {
  text-align: center;
  color: #9ca3af;
  font-size: 14px;
  padding: 30px 0;
}

</style>