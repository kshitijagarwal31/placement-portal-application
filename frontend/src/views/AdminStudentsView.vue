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
        placeholder="Search by name or email..."
      />
    </div>

    <div class="table-box">
      <table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Name</th>
            <th>Email</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(student, index) in filteredStudents" :key="student.id">
            <td>{{ index + 1 }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.email }}</td>
            <td>
              <span :class="student.is_active ? 'badge-active' : 'badge-blacklisted'">
                {{ student.is_active ? 'Active' : 'Blacklisted' }}
              </span>
            </td>
            <td>
              <div class="actions">
                <button class="btn-view" @click="viewProfile(student)">View Profile</button>
                <button
                  v-if="student.is_active"
                  class="btn-blacklist"
                  @click="blacklistStudent(student)"
                >Blacklist</button>
                <button
                  v-else
                  class="btn-view"
                  @click="unblacklistStudent(student)"
                >Unblacklist</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <div v-if="filteredStudents.length === 0" class="empty">
        No students found
      </div>
    </div>

    <div v-if="selectedStudent" class="modal-overlay" @click.self="selectedStudent = null">
      <div class="modal">

        <div class="modal-header">
          <h3>Student Profile</h3>
          <button class="btn-close" @click="selectedStudent = null">✕</button>
        </div>

        <div class="detail-top">
          <div class="avatar-lg">{{ selectedStudent.name.charAt(0) }}</div>
          <div>
            <h4>{{ selectedStudent.name }}</h4>
            <p>{{ selectedStudent.college }} · CGPA {{ selectedStudent.cgpa }}</p>
          </div>
          <span :class="selectedStudent.is_active ? 'badge-active' : 'badge-blacklisted'">
            {{ selectedStudent.is_active ? 'Active' : 'Blacklisted' }}
          </span>
        </div>

        <div class="detail-rows">
          <div class="detail-row">
            <span class="detail-label">Name</span>
            <span class="detail-value">{{ selectedStudent.name }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Username</span>
            <span class="detail-value">{{ selectedStudent.username }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Email</span>
            <span class="detail-value">{{ selectedStudent.email }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">CGPA</span>
            <span class="detail-value">{{ selectedStudent.cgpa }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">College</span>
            <span class="detail-value">{{ selectedStudent.college }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Skills</span>
            <span class="detail-value">{{ selectedStudent.skills }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Resume</span>
            <a :href="selectedStudent.resume" target="_blank" class="resume-link">📄 View Resume</a>
          </div>
        </div>

        <div class="app-section">
          <h4 class="app-section-title">
            Applied Drives
            <span class="app-count">{{ studentApplications.length }}</span>
          </h4>

          <div v-if="studentApplications.length === 0" class="app-empty">
            No applications yet
          </div>

          <div class="app-table-box" v-else>
            <table class="app-table">
              <thead>
                <tr>
                  <th>S.No</th>
                  <th>Company</th>
                  <th>Role</th>
                  <th>Applied On</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(app, index) in studentApplications" :key="app.id">
                  <td>{{ index + 1 }}</td>
                  <td>{{ app.company }}</td>
                  <td>{{ app.drive }}</td>
                  <td>{{ app.date }}</td>
                  <td>
                    <span :class="[
                      'status-badge',
                      app.status === 'Pending'     ? 'status-pending'     :
                      app.status === 'Shortlisted' ? 'status-shortlisted' :
                      app.status === 'Selected'    ? 'status-selected'    :
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
import axios from "axios"

export default {
  name: "AdminStudentsView",

  data() {
    return {
      search: "",
      selectedStudent: null,
      students: [],
      loading: false
    }
  },

  async mounted() {
    const token = localStorage.getItem("token")
    const res = await axios.get("http://localhost:5000/admin/students", {
      headers: { "Authentication-Token": token }
    })
    this.students = res.data.students
  },

  computed: {
    filteredStudents() {
      const q = this.search.toLowerCase()
      return this.students.filter(s =>
        s.name.toLowerCase().includes(q) ||
        s.email.toLowerCase().includes(q) ||
        (s.is_active ? 'active' : 'blacklisted').includes(q)
      )
    },
    studentApplications() {
      if (!this.selectedStudent) return []
      return this.selectedStudent.applications || []
    }
  },

  methods: {
    viewProfile(student) {
      this.selectedStudent = student
    },

    async blacklistStudent(student) {
      const token = localStorage.getItem("token")
      await axios.post(`http://localhost:5000/admin/student/blacklist/${student.id}`, {}, {
        headers: { "Authentication-Token": token }
      })
      student.is_active = false
    },

    async unblacklistStudent(student) {
      const token = localStorage.getItem("token")
      await axios.post(`http://localhost:5000/admin/student/unblacklist/${student.id}`, {}, {
        headers: { "Authentication-Token": token }
      })
      student.is_active = true
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

.badge-active {
  background: #dcfce7;
  color: #16a34a;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.badge-blacklisted {
  background: #fee2e2;
  color: #dc2626;
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

.resume-link {
  color: #2563eb;
  font-weight: 600;
  font-size: 14px;
  text-decoration: none;
}

.resume-link:hover {
  text-decoration: underline;
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

.status-pending {
  background: #fef9c3;
  color: #ca8a04;
}

.status-shortlisted {
  background: #dbeafe;
  color: #2563eb;
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