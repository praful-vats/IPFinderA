const newBookBtn = document.getElementById("new-book-btn");
const submitBtn = document.getElementById("submit-btn");
const newBookForm = document.getElementById("form");
let library = [];

class Book {
  constructor(title, author, status) {
    this.title = title;
    this.author = author;
    this.status = status;
  }
}
// Display book entry form when 'New Book' button is clicked
newBookBtn.addEventListener("click", function() {
  const bookWrapper = document.querySelector(".button-wrapper");
  if (newBookForm.style.display == "none") {
    newBookForm.style.display = "block";
  }
});

// Create new Book object and add to library array
function addBookToLibrary() {
  // Pop previous Book to avoid duplicate entries
  if (library.length > 0) {
    library.pop();
  }
  const titleField = document.getElementById("title-form").value;
  const authorField = document.getElementById("author-form").value;
  const readRadios = document.getElementsByName("read-form").value;

  // Toggle read status based on radio button selection

  const newBook = new Book(titleField, authorField, status);
  library.push(newBook);
}

// Update HTML table with new book details
function render() {
  library.map(book => {
    const table = document.getElementById("table");
    const newRow = table.insertRow(-1);
    newRow.className = "row";
    const newCellHostname = newRow.insertCell(-1);
    newCellHostname.className = "cell";
    const renderHostname = document.createTextNode(book.title);

    const newCellAuthor = newRow.insertCell(-1);
    newCellAuthor.className = "cell";
    const renderAuthor = document.createTextNode(book.author);

    const newCellStatus = newRow.insertCell(-1);
    newCellStatus.className = "cell";
    const renderStatus = document.createTextNode(book.status);

//     const newCellStatus = newRow.insertCell(-1);
//     newCellStatus.className = "cell";
//     const renderStatus = document.createTextNode(book.status);

//     const newCellCheckbox = newRow.insertCell(-1);
//     newCellCheckbox.className = "cell";

//     const newCheckbox = document.createElement("input");
//     newCheckbox.type = "checkbox";
//     newCheckbox.className = "delete";

    newCellHostname.appendChild(renderHostname);
    newCellAuthor.appendChild(renderAuthor);
    newCellStatus.appendChild(renderStatus);
  });
}

submitBtn.addEventListener("click", function(e) {
  addBookToLibrary();
  render();
  e.preventDefault(); //prevents refreshing after form submission
});

// delete checked items from library



removeBtn.addEventListener("click", function() {
  const checkboxArr = Array.from(checkbox);
  for (let i = 0; i < checkboxArr.length; i++) {
    if (checkboxArr[i].checked) {
      table.deleteRow(i);
    }
  }
});