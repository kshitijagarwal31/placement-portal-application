<template>

  <div class="applications-page">
    <div class="topbar">
      <div>
        <h1>
          My Applications
        </h1>
        <p>
          Track all your placement applications
        </p>
      </div>
      <input
        v-model="search"
        type="text"
        placeholder="Search by company or drive..."
        class="search-input"
      />
    </div>
    <div class="applications-grid">
      <div
        class="application-card"
        v-for="application in filteredApplications"
        :key="application.id"
      >

        <div class="card-top">
          <div>
            <h2>
              {{ application.drive }}
            </h2>
            <p class="company-name">
              {{ application.company }}
            </p>
          </div>
          <span
            :class="[
              'status-badge',

              application.status === 'Applied'
              ? 'status-applied'

              : application.status === 'Shortlisted'
              ? 'status-shortlisted'

              : application.status === 'Rejected'
              ? 'status-rejected'

              : 'status-selected'
            ]"
          >

            {{ application.status }}
          </span>
        </div>
        <div class="card-details">
          <div class="detail-item">
            <p class="detail-label">
              Applied On
            </p>
            <h4>
              {{ application.date }}
            </h4>
          </div>
          <div class="detail-item">
            <p class="detail-label">
              Package
            </p>
            <h4>
              {{ application.package }}
            </h4>
          </div>
        </div>
        <button class="view-btn">
          View Details
        </button>
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
          drive: "Software Engineer Hiring",
          company: "Google",
          status: "Applied",
          date: "20 May 2026",
          package: "45 LPA"
        },
        {
          id: 2,
          drive: "SDE-1 Recruitment",
          company: "Microsoft",
          status: "Shortlisted",
          date: "18 May 2026",
          package: "40 LPA"
        },
        {
          id: 3,
          drive: "Backend Developer Drive",
          company: "Amazon",
          status: "Rejected",
          date: "15 May 2026",
          package: "35 LPA"
        },
        {
          id: 4,
          drive: "Frontend Hiring",
          company: "Flipkart",
          status: "Selected",
          date: "12 May 2026",
          package: "28 LPA"
        },
        {
          id: 5,
          drive: "Full Stack Developer",
          company: "Zomato",
          status: "Applied",
          date: "22 May 2026",
          package: "18 LPA"
        }
      ]
    }
  },

  computed: {

    filteredApplications() {
      const query = this.search.toLowerCase()
      return this.applications.filter(application =>
        application.company.toLowerCase().includes(query) ||
        application.drive.toLowerCase().includes(query)

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

.applications-page{
  width:100%;
}

.topbar{
  display:flex;
  justify-content:space-between;
  align-items:center;
  gap:20px;
  margin-bottom:28px;
  flex-wrap:wrap;
}

.topbar h1{
  font-size:30px;
  color:#111827;
  margin-bottom:4px;
}

.topbar p{
  color:#6b7280;
  font-size:14px;
}

.search-input{
  width:260px;
  padding:11px 14px;
  border:1px solid #e5e7eb;
  border-radius:10px;
  outline:none;
  font-size:14px;
  transition:0.2s;
  background:white;
}

.search-input:focus{
  border-color:#2563eb;
}

.applications-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
  gap:20px;
}

.application-card{
  background:white;
  border-radius:18px;
  padding:20px;
  border:1px solid #f1f5f9;
  box-shadow:0 4px 12px rgba(0,0,0,0.05);

  display:flex;
  flex-direction:column;
  justify-content:space-between;

  min-height:220px;

  transition:0.2s;
}

.application-card:hover{
  transform:translateY(-3px);
}

.card-top{
  display:flex;
  justify-content:space-between;
  align-items:flex-start;
  gap:12px;
  margin-bottom:18px;
}

.card-top h2{
  font-size:19px;
  color:#111827;
  line-height:1.4;
  margin-bottom:4px;
}

.company-name{
  color:#6b7280;
  font-size:14px;
}

.card-details{
  display:flex;
  gap:12px;
  margin-bottom:18px;
}

.detail-item{
  flex:1;
  background:#f9fafb;
  padding:14px;
  border-radius:12px;
}

.detail-label{
  color:#6b7280;
  font-size:12px;
  margin-bottom:6px;
}

.detail-item h4{
  color:#111827;
  font-size:14px;
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

.status-badge{
  padding:6px 12px;
  border-radius:20px;
  font-size:12px;
  font-weight:600;
  white-space:nowrap;
}

.status-applied{
  background:#dbeafe;
  color:#2563eb;
}

.status-shortlisted{
  background:#fef3c7;
  color:#d97706;
}

.status-rejected{
  background:#fee2e2;
  color:#dc2626;
}

.status-selected{
  background:#dcfce7;
  color:#16a34a;
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

  .card-details{
    flex-direction:column;
  }

}

</style>