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
              <button class="btn-view" @click="$router.push('/student_dashboard/application_detail')">View Details</button>
            </td>
          </tr>
        </tbody>
      </table>

      <div v-if="filteredApplications.length === 0" class="empty">
        No applications found
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
      applications: [
        {
          id: 1,
          company: "Google",
          drive: "Software Engineer Hiring",
          date: "20 May 2026",
          package: "45 LPA",
          status: "Applied"
        },
        {
          id: 2,
          company: "Microsoft",
          drive: "SDE-1 Recruitment",
          date: "18 May 2026",
          package: "40 LPA",
          status: "Shortlisted"
        },
        {
          id: 3,
          company: "Amazon",
          drive: "Backend Developer Drive",
          date: "15 May 2026",
          package: "35 LPA",
          status: "Rejected"
        },
        {
          id: 4,
          company: "Flipkart",
          drive: "Frontend Hiring",
          date: "12 May 2026",
          package: "28 LPA",
          status: "Selected"
        },
        {
          id: 5,
          company: "Zomato",
          drive: "Full Stack Developer",
          date: "22 May 2026",
          package: "18 LPA",
          status: "Applied"
        }
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
      if (status === 'Selected') return 'badge-selected'
      if (status === 'Shortlisted') return 'badge-shortlisted'
      if (status === 'Rejected') return 'badge-rejected'
      return 'badge-applied'
    },

    viewDetails(app) {
      this.$router.push(`/student/application/${app.id}`)
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

</style>