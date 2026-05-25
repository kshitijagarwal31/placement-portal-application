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
              <button class="btn-view" @click="$router.push('/admin_dashboard/application_detail')">View</button>
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
  name: "AdminApplicationsView",

  data() {
    return {
      search: "",
      applications: [
        { id: 1, student: "Rahul Sharma",  company: "Google",    role: "Software Engineer",   appliedOn: "10 May 2026", status: "Selected" },
        { id: 2, student: "Priya Singh",   company: "Microsoft", role: "SDE-1",               appliedOn: "11 May 2026", status: "Pending"  },
        { id: 3, student: "Amit Kumar",    company: "Amazon",    role: "Backend Developer",   appliedOn: "12 May 2026", status: "Rejected" },
        { id: 4, student: "Sneha Verma",   company: "Flipkart",  role: "Frontend Developer",  appliedOn: "13 May 2026", status: "Selected" },
        { id: 5, student: "Rohan Gupta",   company: "Zomato",    role: "Full Stack Developer", appliedOn: "14 May 2026", status: "Pending"  },
        { id: 6, student: "Pooja Yadav",   company: "Infosys",   role: "Systems Engineer",    appliedOn: "15 May 2026", status: "Selected" },
        { id: 7, student: "Vikram Patel",  company: "TCS",       role: "Developer",           appliedOn: "16 May 2026", status: "Rejected" },
        { id: 8, student: "Anjali Mishra", company: "Wipro",     role: "Junior Developer",    appliedOn: "17 May 2026", status: "Pending"  },
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

</style>