<template>
  <div>

    <button class="btn-back" @click="$router.back()">← Back</button>

    <div class="profile-box">

      <div class="profile-header">
        <div class="avatar">{{ drive.job_title.charAt(0) }}</div>
        <div>
          <h1>{{ drive.job_title }}</h1>
          <p>{{ drive.company }} · {{ drive.salary }}</p>
        </div>
        <span :class="
          drive.status === 'Pending'   ? 'badge-pending'   :
          drive.status === 'Upcoming'  ? 'badge-upcoming'  :
          drive.status === 'Ongoing'   ? 'badge-ongoing'   :
          drive.status === 'Completed' ? 'badge-completed' :
          'badge-rejected'
        ">{{ drive.status }}</span>
      </div>

      <div class="info-grid">
        <div class="info-item">
          <p class="info-label">Company</p>
          <p class="info-value">{{ drive.company }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Package</p>
          <p class="info-value">{{ drive.salary }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Start Date</p>
          <p class="info-value">{{ drive.start_date }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Last Date</p>
          <p class="info-value">{{ drive.last_date }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Skills Required</p>
          <p class="info-value">{{ drive.skills_required }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Description</p>
          <p class="info-value">{{ drive.job_description }}</p>
        </div>
      </div>

    </div>

    <div class="section-title">
      <h2>Applications</h2>
      <p>All students who applied for this drive</p>
    </div>

    <div class="table-box">
      <table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Student</th>
            <th>Branch</th>
            <th>CGPA</th>
            <th>Apply Date</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(app, index) in drive.applications" :key="app.id">
            <td>{{ index + 1 }}</td>
            <td>{{ app.student }}</td>
            <td>{{ app.branch }}</td>
            <td>{{ app.cgpa }}</td>
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

      <div v-if="drive.applications.length === 0" class="empty">
        No applications found
      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: "AdminPlacementDriveDetailView",

  data() {
    return {
      drive: {
        id: 1,
        job_title: "Software Engineer",
        company: "Google",
        salary: "45 LPA",
        start_date: "25 May 2026",
        last_date: "30 May 2026",
        skills_required: "Python, DSA, System Design",
        job_description: "Looking for strong problem solvers.",
        status: "Upcoming",
        applications: [
          { id: 1, student: "Rahul Sharma", branch: "CSE", cgpa: "8.9", apply_date: "10 May 2026", status: "Pending"  },
          { id: 2, student: "Priya Singh",  branch: "ECE", cgpa: "7.5", apply_date: "11 May 2026", status: "Selected" },
          { id: 3, student: "Amit Kumar",   branch: "ME",  cgpa: "8.1", apply_date: "12 May 2026", status: "Rejected" },
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
  padding: 16px 20px;
  text-align: left;
  font-size: 14px;
  color: #6b7280;
  font-weight: 600;
  border-bottom: 1px solid #e5e7eb;
}

td {
  padding: 16px 20px;
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

.badge-pending {
  background: #fef9c3;
  color: #ca8a04;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.badge-upcoming {
  background: #dbeafe;
  color: #2563eb;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.badge-ongoing {
  background: #fef9c3;
  color: #ca8a04;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.badge-completed {
  background: #f3f4f6;
  color: #6b7280;
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