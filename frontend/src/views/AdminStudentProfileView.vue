<template>
  <div>

    <button class="btn-back" @click="$router.back()">← Back</button>

    <div class="profile-box">

      <div class="profile-header">
        <div class="avatar">{{ student.name.charAt(0) }}</div>
        <div>
          <h1>{{ student.name }}</h1>
          <p>{{ student.email }} · {{ student.username }}</p>
        </div>
        <span :class="student.is_active ? 'badge-active' : 'badge-blacklisted'">
          {{ student.is_active ? 'Active' : 'Blacklisted' }}
        </span>
      </div>

      <div class="info-grid">
        <div class="info-item">
          <p class="info-label">College</p>
          <p class="info-value">{{ student.college_name || '—' }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">CGPA</p>
          <p class="info-value">{{ student.cgpa }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Skills</p>
          <p class="info-value">{{ student.skills }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Bio</p>
          <p class="info-value">{{ student.bio }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Resume</p>
          <p class="info-value">
            <a :href="student.resume" target="_blank" class="resume-link">View Resume</a>
          </p>
        </div>
      </div>

    </div>

    <div class="section-title">
      <h2>Applications</h2>
      <p>All drives this student applied to</p>
    </div>

    <div class="table-box">
      <table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Drive</th>
            <th>Company</th>
            <th>Apply Date</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(app, index) in student.applications" :key="app.id">
            <td>{{ index + 1 }}</td>
            <td>{{ app.drive }}</td>
            <td>{{ app.company }}</td>
            <td>{{ app.apply_date }}</td>
            <td>
              <span :class="
                app.status === 'Pending'  ? 'badge-pending'  :
                app.status === 'Selected' ? 'badge-selected' :
                'badge-rejected'
              ">{{ app.status }}</span>
            </td>
          </tr>
        </tbody>
      </table>

      <div v-if="student.applications.length === 0" class="empty">
        No applications found
      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: "AdminStudentProfileView",

  data() {
    return {
      student: {
        id: 1,
        name: "Rahul Sharma",
        username: "rahul123",
        email: "rahul@college.com",
        is_active: true,
        college_name: "IIT Delhi",
        cgpa: 8.9,
        skills: "Vue, Python, Java, javascript, docker, aws, flask and many more",
        bio: "Passionate developer looking for opportunities.",
        resume: "#",
        applications: [
          { id: 1, drive: "Software Engineer",  company: "Google",    apply_date: "10 May 2026", status: "Pending"  },
          { id: 2, drive: "Frontend Developer", company: "Microsoft", apply_date: "11 May 2026", status: "Selected" },
          { id: 3, drive: "Backend Developer",  company: "Amazon",    apply_date: "12 May 2026", status: "Rejected" },
        ]
      }
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

.btn-back {
  background: none;
  border: none;
  color: #2563eb;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  margin-bottom: 20px;
  padding: 0;
}

.btn-back:hover {
  text-decoration: underline;
}

.profile-box {
  background: white;
  border-radius: 18px;
  padding: 24px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  margin-bottom: 28px;
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 1px solid #f3f4f6;
}

.avatar {
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

.profile-header h1 {
  font-size: 18px;
  color: #111827;
  font-weight: 600;
  margin-bottom: 4px;
}

.profile-header p {
  font-size: 13px;
  color: #6b7280;
}

.profile-header span {
  margin-left: auto;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 14px;
}

.info-item {
  background: #f9fafb;
  padding: 14px;
  border-radius: 10px;
}

.info-label {
  font-size: 12px;
  color: #6b7280;
  margin-bottom: 6px;
}

.info-value {
  font-size: 14px;
  color: #111827;
  font-weight: 600;
}

.resume-link {
  color: #2563eb;
  text-decoration: none;
  font-weight: 600;
}

.resume-link:hover {
  text-decoration: underline;
}

.section-title {
  margin-bottom: 16px;
}

.section-title h2 {
  font-size: 18px;
  color: #111827;
  font-weight: 600;
  margin-bottom: 4px;
}

.section-title p {
  font-size: 13px;
  color: #6b7280;
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
  padding: 14px 20px;
  text-align: left;
  font-size: 14px;
  color: #6b7280;
  font-weight: 600;
  border-bottom: 1px solid #e5e7eb;
}

td {
  padding: 14px 20px;
  font-size: 14px;
  color: #111827;
  border-bottom: 1px solid #f3f4f6;
}

tr:last-child td {
  border-bottom: none;
}

tr:hover td {
  background: #f9fafb;
}

.empty {
  text-align: center;
  color: #9ca3af;
  font-size: 15px;
  padding: 40px 0;
}

.badge-active {
  background: #dcfce7;
  color: #16a34a;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.badge-blacklisted {
  background: #fee2e2;
  color: #dc2626;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.badge-pending {
  background: #fef9c3;
  color: #ca8a04;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.badge-selected {
  background: #dcfce7;
  color: #16a34a;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.badge-rejected {
  background: #fee2e2;
  color: #dc2626;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

</style>