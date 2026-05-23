<template>

  <div>
    <div class="topbar">
      <div>
        <h1>
          Placement Drives
        </h1>
        <p>
          All available placement drives
        </p>
      </div>
      <input
        v-model="search"
        class="search-input"
        type="text"
        placeholder="Search by company or drive..."
      />
    </div>
    <div class="drives-grid">
      <div
        class="drive-card"
        v-for="drive in filteredDrives"
        :key="drive.id"
      >
        <div class="card-top">
          <h2>
            {{ drive.company }}
          </h2>
          <span :class="
            drive.status === 'Upcoming'
              ? 'badge-upcoming'
              : drive.status === 'Ongoing'
              ? 'badge-ongoing'
              : 'badge-completed'
          ">
            {{ drive.status }}
          </span>
        </div>
        <div class="card-content">
          <p>
            <strong>
              Drive:
            </strong>
            {{ drive.role }}
          </p>
          <p>
            <strong>
              End Date:
            </strong>
            {{ drive.date }}
          </p>
        </div>
        <div class="card-bottom">
          <button class="view-btn">
            View Details
          </button>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "StudentPlacementDrivesView",

  data() {
    return {
      search: "",
      drives: [
        {
          id: 1,
          company: "Google",
          role: "Software Engineer",
          date: "25 May 2026",
          status: "Upcoming"
        },
        {
          id: 2,
          company: "Microsoft",
          role: "SDE-1",
          date: "28 May 2026",
          status: "Upcoming"
        },
        {
          id: 3,
          company: "Amazon",
          role: "Backend Developer",
          date: "20 May 2026",
          status: "Ongoing"
        },
        {
          id: 4,
          company: "Flipkart",
          role: "Frontend Developer",
          date: "30 May 2026",
          status: "Upcoming"
        },
        {
          id: 5,
          company: "Zomato",
          role: "Full Stack Developer",
          date: "18 May 2026",
          status: "Ongoing"
        },
        {
          id: 6,
          company: "Infosys",
          role: "Systems Engineer",
          date: "15 May 2026",
          status: "Completed"
        },
        {
          id: 7,
          company: "TCS",
          role: "Developer",
          date: "10 May 2026",
          status: "Completed"
        },
        {
          id: 8,
          company: "Wipro",
          role: "Junior Developer",
          date: "22 May 2026",
          status: "Upcoming"
        }
      ]
    }
  },
  computed: {

    filteredDrives() {
      const q = this.search.toLowerCase()
      return this.drives.filter(drive =>
        drive.company.toLowerCase().includes(q) ||
        drive.role.toLowerCase().includes(q)
      )
    }
  }
}

</script>

<style scoped>

*{
  margin:0;
  padding:0;
  box-sizing:border-box;
}

.topbar{
  display:flex;
  justify-content:space-between;
  align-items:center;
  gap:20px;
  margin-bottom:30px;
  flex-wrap:wrap;
}

.topbar h1{
  font-size:30px;
  color:#111827;
  margin-bottom:5px;
}

.topbar p{
  color:#6b7280;
  font-size:14px;
}

.search-input{
  width:260px;
  padding:11px 14px;
  border:1px solid #e5e7eb;
  border-radius:12px;
  outline:none;
  font-size:14px;
  transition:0.2s;
  background:white;
}

.search-input:focus{
  border-color:#2563eb;
}

.drives-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(290px,1fr));
  gap:20px;
}

.drive-card{
  background:white;
  border:1px solid #f1f5f9;
  border-radius:18px;
  padding:20px;

  display:flex;
  flex-direction:column;
  justify-content:space-between;

  min-height:220px;

  box-shadow:0 3px 12px rgba(0,0,0,0.04);

  transition:0.2s;
}

.drive-card:hover{
  transform:translateY(-3px);
}

.card-top{
  display:flex;
  justify-content:space-between;
  align-items:flex-start;
  gap:10px;
  margin-bottom:20px;
}

.card-top h2{
  font-size:20px;
  color:#111827;
  line-height:1.4;
}

.card-content{
  flex:1;
  margin-bottom:20px;
}

.card-content p{
  font-size:14px;
  color:#4b5563;
  margin-bottom:12px;
  line-height:1.6;
}

.view-btn{
  width:100%;
  border:none;
  background:#2563eb;
  color:white;
  padding:11px;
  border-radius:10px;
  font-size:14px;
  font-weight:600;
  cursor:pointer;
  transition:0.2s;
}

.view-btn:hover{
  background:#1d4ed8;
}

.badge-upcoming,
.badge-ongoing,
.badge-completed{
  padding:6px 12px;
  border-radius:20px;
  font-size:12px;
  font-weight:600;
  white-space:nowrap;
}

.badge-upcoming{
  background:#dbeafe;
  color:#2563eb;
}

.badge-ongoing{
  background:#fef3c7;
  color:#ca8a04;
}

.badge-completed{
  background:#f3f4f6;
  color:#6b7280;
}

@media(max-width:700px){

  .topbar{
    flex-direction:column;
    align-items:flex-start;
  }

  .search-input{
    width:100%;
  }

  .topbar h1{
    font-size:26px;
  }

}

</style>