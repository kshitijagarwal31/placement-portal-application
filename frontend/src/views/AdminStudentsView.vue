<template>
  <div>

    <div class="topbar">
      <div>
        <h1>Students</h1>
        <p>All registered students</p>
      </div>
      <input
        v-model="search"
        class="search-input"
        type="text"
        placeholder="Search by name, email or branch..."
      />
    </div>

    <div class="table-box">
      <table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Name</th>
            <th>Email</th>
            <th>Branch</th>
            <th>CGPA</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(student, index) in filteredStudents" :key="student.id">
            <td>{{ index + 1 }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.email }}</td>
            <td>{{ student.branch }}</td>
            <td>{{ student.cgpa }}</td>
            <td>
              <span :class="student.placed ? 'badge-placed' : 'badge-pending'">
                {{ student.placed ? 'Placed' : 'Pending' }}
              </span>
            </td>
            <td>
              <div class="actions">
                <button class="btn-view">View Profile</button>
                <button class="btn-blacklist" @click="blacklistStudent(student)">Blacklist</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

  </div>
</template>

<script>
export default {
  name: "AdminStudentsView",

  data() {
    return {
      search: "",
      students: [
        { id: 1, name: "Rahul Sharma",  email: "rahul@college.com",  branch: "CSE", cgpa: "8.9", placed: true  },
        { id: 2, name: "Priya Singh",   email: "priya@college.com",  branch: "ECE", cgpa: "7.5", placed: false },
        { id: 3, name: "Amit Kumar",    email: "amit@college.com",   branch: "ME",  cgpa: "8.1", placed: true  },
        { id: 4, name: "Sneha Verma",   email: "sneha@college.com",  branch: "CSE", cgpa: "9.2", placed: true  },
        { id: 5, name: "Rohan Gupta",   email: "rohan@college.com",  branch: "IT",  cgpa: "7.8", placed: false },
        { id: 6, name: "Pooja Yadav",   email: "pooja@college.com",  branch: "CSE", cgpa: "8.4", placed: true  },
        { id: 7, name: "Vikram Patel",  email: "vikram@college.com", branch: "EE",  cgpa: "7.2", placed: false },
        { id: 8, name: "Anjali Mishra", email: "anjali@college.com", branch: "CSE", cgpa: "9.0", placed: true  },
      ]
    }
  },

  computed: {
    filteredStudents() {
      const q = this.search.toLowerCase()
      return this.students.filter(s =>
        s.name.toLowerCase().includes(q) ||
        s.email.toLowerCase().includes(q) ||
        s.branch.toLowerCase().includes(q)
      )
    }
  },

  methods: {
    blacklistStudent(student) {
      student.placed = false
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
  margin-bottom: 5px;
}

.topbar p {
  color: #6b7280;
  font-size: 15px;
}

.search-input {
  padding: 10px 16px;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  font-size: 14px;
  color: #111827;
  width: 280px;
  outline: none;
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

.btn-blacklist {
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

.btn-blacklist:hover {
  background: #fecaca;
}

.badge-placed {
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

</style>