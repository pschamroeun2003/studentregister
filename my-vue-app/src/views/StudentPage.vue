<template>
    <div class="full-screen">
        <h1 id="topic" class="text-2xl font-semibold mb-4">Student Management</h1>
        <div class="overflow-x-auto">
            <table class="min-w-full table-auto bg-white shadow-md rounded-lg overflow-hidden">
                <thead>
                    <tr class="bg-gray-100 text-left text-sm font-semibold text-gray-600">
                        <th class="py-2 px-4 border">Firstname</th>
                        <th class="py-2 px-4 border">Lastname</th>
                        <th class="py-2 px-4 border">Date Of Birth</th>
                        <th class="py-2 px-4 border">Gender</th>
                        <th class="py-2 px-4 border">Email</th>
                        <th class="py-2 px-4 border">Phone</th>
                        <th class="py-2 px-4 border">Address</th>
                        <th class="py-2 px-4 border">Created At</th>
                        <th class="py-2 px-4 border">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="hover:bg-gray-50">
                        <td class="py-2 px-4 border">John</td>
                        <td class="py-2 px-4 border">Doe</td>
                        <td class="py-2 px-4 border">01/01/2000</td>
                        <td class="py-2 px-4 border">Male</td>
                        <td class="py-2 px-4 border">johndoe@example.com</td>
                        <td class="py-2 px-4 border">+123456789</td>
                        <td class="py-2 px-4 border">123 Street, City</td>
                        <td class="py-2 px-4 border">01/01/2022</td>
                        <td class="py-2 px-4 border text-center">
                            <button class="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600">Update</button>
                            <button
                                class="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600 ml-2">Delete</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script lang="ts">
export default {
    name: 'StudentPage',
};
</script>

<style scoped>

@font-face {
    font-family: 'ArialCustom';
    src: url('@/assets/fonts/arialceb.ttf') format('truetype');
}

html,
body {
    height: 100%;
    margin: 0;
    font-family: 'ArialCustom', Arial, sans-serif;
}
#topic{
    font-family: 'ArialCustom', Arial, sans-serif;
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
    font-family: 'ArialCustom', Arial, sans-serif;
}

/* Striped rows */
tr:nth-child(even) {
    background-color: #f9fafb;
}

/* Hover effect */
tr:hover {
    background-color: #f1f5f9;
}
</style>
