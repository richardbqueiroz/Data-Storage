document.addEventListener("DOMContentLoaded", function () {
  const availablePermissions = document.getElementById("available_permissions");
  const selectedPermissions = document.getElementById("selected_permissions");
  const addPermissionButton = document.getElementById("add_permission");
  const removePermissionButton = document.getElementById("remove_permission");

  addPermissionButton.addEventListener("click", function () {
      moveOptions(availablePermissions, selectedPermissions);
  });

  removePermissionButton.addEventListener("click", function () {
      moveOptions(selectedPermissions, availablePermissions);
  });

  function moveOptions(from, to) {
      Array.from(from.selectedOptions).forEach(option => {
          to.appendChild(option);
      });
  }

  document.querySelector("form").addEventListener("submit", function () {
      Array.from(selectedPermissions.options).forEach(option => {
          option.selected = true;
      });
  });
});
