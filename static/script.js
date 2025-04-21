document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".card");
  
    cards.forEach(card => {
      const editBtn = card.querySelector(".edit-btn");
      const cancelBtn = card.querySelector(".cancel-btn");
      const form = card.querySelector(".edit-form");
      const content = card.querySelector(".note-content");
  
      editBtn.addEventListener("click", () => {
        form.classList.remove("d-none");
        content.classList.add("d-none");
      });
  
      cancelBtn.addEventListener("click", () => {
        form.classList.add("d-none");
        content.classList.remove("d-none");
      });
  
      form.addEventListener("submit", async (e) => {
        e.preventDefault();
  
        const id = card.getAttribute("data-id");
        const title = form.querySelector(".edit-title").value.trim();
        const desc = form.querySelector(".edit-desc").value.trim();
        const important = form.querySelector(".edit-important").checked;
  
        const response = await fetch(`/update/${id}`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ title, desc, important }),
        });
  
        if (response.ok) {
          window.location.reload(); // reload to reflect updated values
        } else {
          alert("Failed to update note");
        }
      });
    });
  });
  