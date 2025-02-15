<template>
  <div class="full-screen">
    <h1 id="topic" class="text-2xl font-semibold mb-4">Course</h1>

    <LoadingSpinner :isLoading="loading" />

    <div class="button-container">
      <button class="create-button" @click="openModal">Create</button>
    </div>

    <div v-if="isModalOpen" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <h2 id="titlemodel">{{ isEditMode ? 'Update Course' : 'Create New Course' }}</h2>
        <form @submit.prevent="saveCourse">
          <div class="form-group">
            <label for="courseName">Course Name</label>
            <input id="courseName" v-model="newCourse.course_name" type="text" class="form-control"
              placeholder="Course Name" required />
          </div>
          <div class="form-group">
            <label for="courseCode">Code</label>
            <input id="courseCode" v-model="newCourse.code" type="text" class="form-control" placeholder="Course Code"
              required />
          </div>
          <div class="form-group">
            <label for="credits">Credits</label>
            <input id="credits" v-model="newCourse.credits" type="text" class="form-control" placeholder="Credits"
              required />
          </div>
          <div class="form-group">
            <label for="department">Department</label>
            <select id="department" v-model="newCourse.department" class="form-control" required>
              <option value="" disabled selected>Select a Department</option>
              <option value="Engineering">Engineering</option>
              <option value="Science">Science</option>
              <option value="Arts">Arts</option>
              <option value="Business">Business</option>
              <option value="Information Technology">Information Technology</option>
            </select>
          </div>
          <button type="submit" class="btn btn-primary">{{ isEditMode ? 'Update' : 'Create' }} Course</button>
        </form>
      </div>
    </div>
    <div class="overflow-x-auto">
      <table class="min-w-full table-auto bg-white shadow-md rounded-lg overflow-hidden">
        <thead>
          <tr class="bg-gray-100 text-left text-sm font-semibold text-gray-600">
            <th class="py-2 px-4 border">Name</th>
            <th class="py-2 px-4 border">Code</th>
            <th class="py-2 px-4 border">Credits</th>
            <th class="py-2 px-4 border">Department</th>
            <th class="py-2 px-4 border">Created At</th>
            <th class="py-2 px-4 border">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="course in courses" :key="course.id" class="hover:bg-gray-50">
            <td class="py-2 px-4 border">{{ course.course_name }}</td>
            <td class="py-2 px-4 border">{{ course.code }}</td>
            <td class="py-2 px-4 border">{{ course.credits }}</td>
            <td class="py-2 px-4 border">{{ course.department }}</td>
            <td class="py-2 px-4 border">{{ course.created_at }}</td>
            <td class="py-2 px-4 border text-center">
              <button class="success-button" @click="updateCourse(course.id)">Update</button>
              <button class="danger-button" @click="deleteCourse(course.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import Swal from "sweetalert2";
import { defineComponent, onMounted, ref } from "vue";
import LoadingSpinner from "../components/LoadingSpinner.vue";

export default defineComponent({
  name: "CoursePage",
  components: {
    LoadingSpinner,
  },
  setup() {
    const courses = ref([]);
    const errorMessage = ref("");
    const loading = ref(true);
    const baseUrl = import.meta.env.VITE_APP_BASE_URL || "http://127.0.0.1:5000";
    const isModalOpen = ref(false);
    const newCourse = ref({
      course_name: "",
      code: "",
      credits: "",
      department: "",
    });
    onMounted(async () => {
      await fetchCourses();
    });
    const isEditMode = ref(false);
    const currentCourseId = ref(null);
    const fetchCourses = async () => {
      try {
        loading.value = true;
        const response = await axios.get(`${baseUrl}/api/courses/course`);
        courses.value = response.data.courses || [];
      } catch (error) {
        errorMessage.value = `Error fetching courses: ${error.message}`;
        console.error("Error fetching courses:", error);
      } finally {
        loading.value = false;
      }
    };

    const saveCourse = async () => {
      try {
        let response;
        if (isEditMode.value) {
          // Update course if in edit mode
          response = await axios.put(`${baseUrl}/api/courses/${currentCourseId.value}`, newCourse.value);
          Swal.fire({
            title: "Updated!",
            text: "The course has been updated.",
            icon: "success",
          });
        } else {
          // Create new course if not in edit mode
          response = await axios.post(`${baseUrl}/api/courses/course`, newCourse.value);
          Swal.fire({
            title: "Success!",
            text: "The course has been created.",
            icon: "success",
          });
        }

        fetchCourses(); // Refresh course list
        closeModal();
      } catch (error) {
        Swal.fire({
          title: "Error!",
          text: `Failed to save the course: ${error.response?.data?.message || 'Unknown error'}`,
          icon: "error",
        });
      }
    };
    const openModal = () => {
      isModalOpen.value = true;
    };
    // Close Modal
    const closeModal = () => {
      isModalOpen.value = false;
      newCourse.value = {
        course_name: "",
        code: "",
        credits: "",
        department: "",
      };
    };
    const deleteCourse = async (id: number) => {
      const result = await Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#d33",
        cancelButtonColor: "#3085d6",
        confirmButtonText: "Yes, delete it!"
      });
      if (result.isConfirmed) {
        try {
          await axios.delete(`${baseUrl}/api/courses/${id}`);
          courses.value = courses.value.filter((course) => course.id !== id);
          Swal.fire({
            title: "Deleted!",
            text: "The course has been deleted.",
            icon: "success",
            timer: 2000,
            showConfirmButton: false
          });
        } catch (error) {
          Swal.fire({
            title: "Error!",
            text: "Failed to delete the course.",
            icon: "error",
          });
        }
      }
    };

    const updateCourse = (id: number) => {
      isEditMode.value = true; // Set to edit mode
      currentCourseId.value = id;
      const course = courses.value.find((course) => course.id === id);
      if (course) {
        newCourse.value = { ...course };
        isModalOpen.value = true;
      }
    };
    return {
      courses,
      errorMessage,
      loading,
      isModalOpen,
      newCourse,
      deleteCourse,
      updateCourse,
      openModal,
      closeModal,
      saveCourse,
    };
  },
});
</script>



<style scoped>
@font-face {
  font-family: "ArialCustom";
  src: url("@/assets/fonts/arialceb.ttf") format("truetype");
}

html,
body {
  height: 100%;
  margin: 0;
  font-family: "ArialCustom", Arial, sans-serif;
}
#topic {
  font-family: "ArialCustom", Arial, sans-serif;
}
.full-screen {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding: 10px;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th,
td {
  padding: 10px;
  text-align: left;
  border: 1px solid #e5e7eb;
  font-family: "ArialCustom", Arial, sans-serif;
}

/* Striped rows */
tr:nth-child(even) {
  background-color: #f9fafb;
}

/* Hover effect */
tr:hover {
  background-color: #f1f5f9;
}

.danger-button {
  background-color: red;
  color: white;
  padding: 10px 20px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.success-button {
  background-color: green;
  color: white;
  padding: 10px 20px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.button-container {
  display: flex;
  justify-content: flex-end;
  /* Aligns to the right */
  padding: 10px;
  /* Optional spacing */
}

.create-button {
  background-color: blue;
  color: white;
  padding: 10px 20px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.create-button:hover {
  background-color: darkblue;
}
/* Modal Overlay */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1050;
  /* Ensures it's on top */
}

/* Modal Content */
.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  width: 500px;
  max-width: 100%;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Bootstrap-like Form Inputs */
.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 0.5rem;
  font-family: "ArialCustom", Arial, sans-serif;
}

button{
  font-family: "ArialCustom", Arial, sans-serif;
}

.form-control {
  width: 100%;
  padding: 0.75rem 1.25rem;
  font-size: 0.90rem;
  border-radius: 4px;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

.form-control:focus {
  border-color: #007bff;
  outline: none;
  box-shadow: 0 0 0 0.2rem rgba(38, 143, 255, 0.25);
}

/* Modal Buttons */
.btn {
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
}

/* Primary Button (Submit) */
.btn-primary {
  background-color: #007bff;
  color: white;
}

.btn-primary:hover {
  background-color: #0056b3;
}

/* Danger Button (Close) */
.btn-danger {
  background-color: #dc3545;
  color: white;
  border: 1px solid #dc3545;
}

.btn-danger:hover {
  background-color: #c82333;
}

/* Close Modal Button */
.close-modal {
  margin-top: 10px;
}

#titlemodel{
  font-family: "ArialCustom", Arial, sans-serif;
}

/* Modal Fade In Animation */
@keyframes modalFadeIn {
  0% {
    opacity: 0;
    transform: scale(0.95);
  }

  100% {
    opacity: 1;
    transform: scale(1);
  }
}
</style>
