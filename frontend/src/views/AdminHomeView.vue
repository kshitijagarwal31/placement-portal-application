<template>
  <div>

    <div class="topbar">
      <h1>Admin Dashboard</h1>
    </div>

    <div class="cards">
      <div class="card">
        <h2>{{ totalStudents }}</h2>
        <p>Total Students</p>
      </div>
      <div class="card">
        <h2>{{ totalCompanies }}</h2>
        <p>Total Companies</p>
      </div>
      <div class="card">
        <h2>{{ totalDrives }}</h2>
        <p>Placement Drives</p>
      </div>
      <div class="card">
        <h2>{{ totalApplications }}</h2>
        <p>Total Applications</p>
      </div>
      <div class="card">
        <h2>{{ totalPlacements }}</h2>
        <p>Total Placements</p>
      </div>
      <div class="card">
        <h2>{{ placementRate }}%</h2>
        <p>Placement Rate</p>
      </div>
    </div>

    <div class="requests-grid">

      <div class="section-box">
        <div class="section-header">
          <h3>Company Requests</h3>
          <span class="pending-count">{{ pendingCompanies.length }} Pending</span>
        </div>

        <div v-if="pendingCompanies.length === 0" class="empty">
          No pending requests
        </div>

        <div
          v-for="company in pendingCompanies.slice(0, 5)"
          :key="company.id"
          class="request-item"
        >
          <div class="request-left">
            <div class="avatar">{{ company.name.charAt(0) }}</div>
            <div>
              <p class="request-name">{{ company.name }}</p>
              <p class="request-sub">{{ company.industry }} · {{ company.location }}</p>
            </div>
          </div>
          <div class="request-actions">
            <button class="btn-approve" @click="approveCompany(company)">Approve</button>
            <button class="btn-reject"  @click="rejectCompany(company)">Reject</button>
          </div>
        </div>

        <div v-if="pendingCompanies.length > 5" class="view-all">
          Showing 5 of {{ pendingCompanies.length }} — go to Companies page
        </div>
      </div>

      <div class="section-box">
        <div class="section-header">
          <h3>Drive Requests</h3>
          <span class="pending-count">{{ pendingDrives.length }} Pending</span>
        </div>

        <div v-if="pendingDrives.length === 0" class="empty">
          No pending requests
        </div>

        <div
          v-for="drive in pendingDrives.slice(0, 5)"
          :key="drive.id"
          class="request-item"
        >
          <div class="request-left">
            <div class="avatar">{{ drive.company.charAt(0) }}</div>
            <div>
              <p class="request-name">{{ drive.company }}</p>
              <p class="request-sub">{{ drive.role }} · {{ drive.date }}</p>
            </div>
          </div>
          <div class="request-actions">
            <button class="btn-approve" @click="approveDrive(drive)">Approve</button>
            <button class="btn-reject"  @click="rejectDrive(drive)">Reject</button>
          </div>
        </div>

        <div v-if="pendingDrives.length > 5" class="view-all">
          Showing 5 of {{ pendingDrives.length }} — go to Drives page
        </div>
      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: "AdminHomeView",

  data() {
    return {
      students: [
        { id: 1, name: "Rahul Sharma",  placed: true  },
        { id: 2, name: "Priya Singh",   placed: false },
        { id: 3, name: "Amit Kumar",    placed: true  },
        { id: 4, name: "Sneha Verma",   placed: true  },
        { id: 5, name: "Rohan Gupta",   placed: false },
        { id: 6, name: "Pooja Yadav",   placed: true  },
        { id: 7, name: "Vikram Patel",  placed: false },
        { id: 8, name: "Anjali Mishra", placed: true  },
      ],
      applications: [
        { id: 1 }, { id: 2 }, { id: 3 },
        { id: 4 }, { id: 5 }, { id: 6 },
        { id: 7 }, { id: 8 },
      ],
      companies: [
        { id: 1, name: "Google",    industry: "Technology",  location: "Bangalore", status: "Pending" },
        { id: 2, name: "Microsoft", industry: "Technology",  location: "Hyderabad", status: "Pending" },
        { id: 3, name: "Amazon",    industry: "E-Commerce",  location: "Bangalore", status: "Active"  },
        { id: 4, name: "Wipro",     industry: "IT Services", location: "Delhi",     status: "Pending" },
        { id: 5, name: "Flipkart",  industry: "E-Commerce",  location: "Bangalore", status: "Active"  },
        { id: 6, name: "Zomato",    industry: "Food Tech",   location: "Gurgaon",   status: "Pending" },
      ],
      drives: [
        { id: 1, company: "Google",    role: "Software Engineer",    date: "25 May 2026", status: "Pending" },
        { id: 2, company: "Microsoft", role: "SDE-1",                date: "28 May 2026", status: "Pending" },
        { id: 3, company: "Zomato",    role: "Full Stack Developer",  date: "18 May 2026", status: "Active"  },
        { id: 4, company: "Flipkart",  role: "Frontend Developer",   date: "30 May 2026", status: "Pending" },
        { id: 5, company: "Amazon",    role: "Backend Developer",    date: "20 May 2026", status: "Active"  },
        { id: 6, company: "Wipro",     role: "Junior Developer",     date: "22 May 2026", status: "Pending" },
      ]
    }
  },

  computed: {
    totalStudents() {
      return this.students.length
    },
    totalCompanies() {
      return this.companies.filter(c => c.status === 'Active').length
    },
    totalDrives() {
      return this.drives.filter(d => d.status === 'Active').length
    },
    totalApplications() {
      return this.applications.length
    },
    totalPlacements() {
      return this.students.filter(s => s.placed).length
    },
    placementRate() {
      if (this.students.length === 0) return 0
      return Math.round((this.totalPlacements / this.students.length) * 100)
    },
    pendingCompanies() {
      return this.companies.filter(c => c.status === 'Pending')
    },
    pendingDrives() {
      return this.drives.filter(d => d.status === 'Pending')
    }
  },

  methods: {
    approveCompany(company) { company.status = 'Active'   },
    rejectCompany(company)  { company.status = 'Rejected' },
    approveDrive(drive)     { drive.status   = 'Active'   },
    rejectDrive(drive)      { drive.status   = 'Rejected' },
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
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.section-header h3 {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
}

.pending-count {
  background: #fef9c3;
  color: #ca8a04;
  font-size: 13px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 20px;
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

.request-actions {
  display: flex;
  gap: 8px;
}

.btn-approve {
  background: #dcfce7;
  color: #16a34a;
  border: none;
  padding: 7px 14px;
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
  padding: 7px 14px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-reject:hover {
  background: #fecaca;
}

.empty {
  text-align: center;
  color: #9ca3af;
  font-size: 14px;
  padding: 30px 0;
}

.view-all {
  text-align: center;
  color: #9ca3af;
  font-size: 13px;
  margin-top: 14px;
}

</style>