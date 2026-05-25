<template>
  <div>

    <div class="topbar">
      <div>
        <h1>Placement Drives</h1>
        <p>All placement drives</p>
      </div>
      <input
        v-model="search"
        class="search-input"
        type="text"
        placeholder="Search by company, role or status..."
      />
    </div>

    <div class="table-box">
      <table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Company</th>
            <th>Role</th>
            <th>Date</th>
            <th>Package</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(drive, index) in filteredDrives" :key="drive.id">
            <td>{{ index + 1 }}</td>
            <td>{{ drive.company }}</td>
            <td>{{ drive.role }}</td>
            <td>{{ drive.date }}</td>
            <td>{{ drive.package }}</td>
            <td>
              <span :class="
                drive.status === 'Pending'   ? 'badge-pending'   :
                drive.status === 'Active'    ? 'badge-active'    :
                drive.status === 'Rejected'  ? 'badge-rejected'  :
                drive.status === 'Upcoming'  ? 'badge-upcoming'  :
                drive.status === 'Ongoing'   ? 'badge-ongoing'   :
                'badge-completed'
              ">
                {{ drive.status }}
              </span>
            </td>
            <td>
              <div class="actions">

                <template v-if="drive.status === 'Pending'">
                  <button class="btn-approve" @click="approveDrive(drive)">Approve</button>
                  <button class="btn-reject"  @click="rejectDrive(drive)">Reject</button>
                </template>

                <template v-if="drive.status === 'Active' || drive.status === 'Upcoming' || drive.status === 'Ongoing' || drive.status === 'Completed'">
                  <button class="btn-view" @click="$router.push('/admin_dashboard/placement_drive_detail')">View Detail</button>
                </template>

                <template v-if="drive.status === 'Rejected'">
                  <span class="text-rejected">—</span>
                </template>

              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <div v-if="filteredDrives.length === 0" class="empty">
        No drives found
      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: "AdminPlacementDrivesView",

  data() {
    return {
      search: "",
      drives: [
        { id: 1, company: "Google",    role: "Software Engineer",   date: "25 May 2026", package: "45 LPA", status: "Pending"   },
        { id: 2, company: "Microsoft", role: "SDE-1",               date: "28 May 2026", package: "40 LPA", status: "Pending"   },
        { id: 3, company: "Amazon",    role: "Backend Developer",   date: "20 May 2026", package: "35 LPA", status: "Ongoing"   },
        { id: 4, company: "Infosys",   role: "Systems Engineer",    date: "15 May 2026", package: "8 LPA",  status: "Completed" },
        { id: 5, company: "TCS",       role: "Developer",           date: "10 May 2026", package: "7 LPA",  status: "Completed" },
        { id: 6, company: "Flipkart",  role: "Frontend Developer",  date: "30 May 2026", package: "28 LPA", status: "Upcoming"  },
        { id: 7, company: "Zomato",    role: "Full Stack Developer", date: "18 May 2026", package: "18 LPA", status: "Pending"   },
        { id: 8, company: "Wipro",     role: "Junior Developer",    date: "12 May 2026", package: "6 LPA",  status: "Completed" },
      ]
    }
  },

  computed: {
    filteredDrives() {
      const q = this.search.toLowerCase()
      return this.drives.filter(d =>
        d.company.toLowerCase().includes(q) ||
        d.role.toLowerCase().includes(q)    ||
        d.status.toLowerCase().includes(q)
      )
    }
  },

  methods: {
    approveDrive(drive) {
      drive.status = 'Active'
    },
    rejectDrive(drive) {
      drive.status = 'Rejected'
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

.btn-approve {
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

.btn-approve:hover {
  background: #bbf7d0;
}

.btn-reject {
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

.btn-reject:hover {
  background: #fecaca;
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

.text-rejected {
  color: #9ca3af;
  font-size: 15px;
}

.badge-pending {
  background: #fef9c3;
  color: #ca8a04;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.badge-active {
  background: #dcfce7;
  color: #16a34a;
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

.badge-upcoming {
  background: #dbeafe;
  color: #2563eb;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.badge-ongoing {
  background: #fef9c3;
  color: #ca8a04;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.badge-completed {
  background: #dcfce7;
  color: #16a34a;
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