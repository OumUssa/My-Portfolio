import jubpetImage from "@/assets/project-img/jubpet.png";
import petSuppliesImage from "@/assets/project-img/pet_supplice.png";
import worksyncImage from "@/assets/project-img/worksync.png";
import hospitalSystemImage from "@/assets/project-img/Hospital_Management_System.png";

// Frontend-only fallback projects, shown automatically when the backend API
// is unreachable so the portfolio never shows a broken/empty state to
// visitors. liveLink holds each project's YouTube demo (auto-embeds on the
// detail page); openProject holds the live/demo site link when one exists.
const staticProjects = [
  {
    id: "static-jubpet",
    adminId: null,
    adminName: "Oum Ussa",
    title: "JubPet — Veterinary Clinic & Appointment Management System",
    desc: "A full-stack veterinary clinic management platform designed to streamline clinical workflows, appointment scheduling, and electronic pet medical records across multiple roles.\n\nCore Highlights\n• Role-Based Access Control — tailored dashboards and permissions for Clinic Admins, Doctors, Receptionists, and Pet Owners.\n• Online Booking System — pet owners browse veterinarians, view real-time availability, and book appointments.\n• Doctor Schedule Management — consultation slots, working hours, and daily patient queues.\n• Receptionist Desk — check-ins, appointment confirmations, status updates, and rescheduling.\n• EMR & Prescription Tracking — centralized digital records for medical history, diagnostics, and follow-up care.\n• Security & Reliability — robust backend validation, error handling, and secure token authentication.\n\nTech Stack: Vue.js, Bootstrap, JavaScript, HTML5/CSS3, Node.js, Express.js, MySQL. Hosted on Contabo Cloud VPS via aaPanel.",
    image: jubpetImage,
    liveLink: "https://youtu.be/AhQPlgPiznE?si=kKafQhhFGTZSL7tn",
    githubLink: "https://github.com/horsenghab/jubpet-backend",
    openProject: "https://jubpet-frontend.g2.ant.com.kh/",
    createdAt: "2025-07-01",
    categories: ["Vue.js", "Node.js", "Express.js", "MySQL"],
    category: "Vue.js",
    tags: ["Vue.js", "Node.js", "Express.js", "MySQL"],
    color: "#6366f1",
  },
  {
    id: "static-pet-supplies",
    adminId: null,
    adminName: "Oum Ussa",
    title: "Pet Supplies — E-Commerce Web Platform",
    desc: "A full-featured e-commerce platform built to streamline online shopping for pet owners, featuring dynamic product filtering, secure inventory management, and an intuitive shopping experience.\n\nCore Highlights\n• Advanced Product Filtering — browse and filter by pet type, category (food, toys, accessories), and price range.\n• Shopping Cart & Checkout — end-to-end purchasing workflow with cart management, order placement, and status tracking.\n• Admin Management Dashboard — full back-office control over products, categories, stock levels, and customer orders.\n• Production Deployment — configured and hosted on a Contabo Cloud VPS managed via aaPanel.\n• Team Collaboration — built with Git/GitHub using structured branching and pull requests.\n\nTech Stack: PHP (Laravel), MySQL, Blade, HTML5, CSS3, Bootstrap, JavaScript.",
    image: petSuppliesImage,
    liveLink: "",
    githubLink: "https://github.com/OumUssa/Pet-Supplice",
    openProject: "https://pet-supplice.vercel.app/",
    createdAt: "2025-05-01",
    categories: ["Laravel", "MySQL", "Bootstrap"],
    category: "Laravel",
    tags: ["Laravel", "MySQL", "Bootstrap"],
    color: "#f97316",
  },
  {
    id: "static-worksync",
    adminId: null,
    adminName: "Oum Ussa",
    title: "WorkSync — Freelance Marketplace & Collaboration Platform",
    desc: "A web platform connecting clients with independent freelancers to streamline remote hiring, project execution, and real-time collaboration.\n\nCore Highlights\n• Dual-Role Onboarding — dedicated workflows for clients (job posting, candidate evaluation) and freelancers (portfolio showcase, skill tagging).\n• Smart Marketplace — dynamic job board with search/filtering and a proposal & bidding system.\n• Direct Communication — real-time messaging and file sharing for negotiations and requirements gathering.\n• Milestone Tracking — integrated dashboards for active contracts, project milestones, and deliverables.\n\nTech Stack: Vue.js, JavaScript, Bootstrap/CSS, Node.js, Express.js, Laravel, MySQL. Tooling: Git, Docker.",
    image: worksyncImage,
    liveLink: "https://youtu.be/qiIQbdQvxGM?si=cb3HTJfRu3g4C1h_",
    githubLink: "https://github.com/OumUssa/WorkSync",
    openProject: "",
    createdAt: "2025-03-01",
    categories: ["Vue.js", "Node.js", "Express.js", "Laravel", "MySQL"],
    category: "Vue.js",
    tags: ["Vue.js", "Node.js", "Express.js", "Laravel", "MySQL"],
    color: "#3b82f6",
  },
  {
    id: "static-hospital-system",
    adminId: null,
    adminName: "Oum Ussa",
    title: "Hospital Management System (HMS)",
    desc: "A desktop management application developed in C/C++ designed to streamline administrative workflows, maintain doctor records, and manage hospital pharmacy inventory.\n\nCore Highlights\n• Doctor Records Management — profiling, specializations, contact details, schedules, and consultation status.\n• Pharmacy & Inventory Control — stock levels, batch numbers, expiry dates, pricing, and automated low-stock alerts.\n• Prescription & Billing Records — links patient prescriptions directly to pharmacy dispensing.\n• Data Persistence — binary/text file I/O to store, search, update, and retrieve records across sessions.\n• CLI Interface — clean, menu-driven console UI with structured input validation and error handling.\n\nTech Stack: C/C++, OOP, Data Structures (Structs/Linked Lists), File I/O Streams. Tooling: GCC/G++, Git.",
    image: hospitalSystemImage,
    liveLink: "https://youtu.be/Im0u7yp5gVE?si=_vOZI2bm_opG3R-3",
    githubLink: "",
    openProject: "https://web.facebook.com/share/v/1KKEfvVeSq/",
    createdAt: "2024-12-01",
    categories: ["C++", "CLI"],
    category: "C++",
    tags: ["C++", "CLI"],
    color: "#14b8a6",
  },
];

export default staticProjects;
