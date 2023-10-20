const array = [];
const list = document.getElementById("list");
const input = document.getElementById("input");
const sortedList = document.getElementById("sortedList");

function addNum() {
  if (isNaN(parseInt(input.value))) {
    input.value = "";
    alert("Enter a valid Number!");
    return;
  }
  array.push(parseInt(input.value));
  input.value = "";
  var option = document.createElement("option");
  option.value = array[array.length - 1];
  option.innerText = array[array.length - 1];
  list.appendChild(option);
}

sortAll = () => {
  const sortedArray = array.sort();
  sortedList.innerText = "";
  for (let i = 0; i < sortedArray.length; i++) {
    const element = sortedArray[i];
    var option = document.createElement("option");
    option.innerText = element;
    option.value = element;
    sortedList.appendChild(option);
  }
}

sort = () => {
  const selectedOptions = [];
  for (const option of list.options) {
    if (option.selected) {
      selectedOptions.push(option.value);
    }
  }
  const sortedArray = selectedOptions.sort();
  sortedList.innerText = "";
  for (let i = 0; i < sortedArray.length; i++) {
    const element = sortedArray[i];
    var option = document.createElement("option");
    option.innerText = element;
    option.value = element;
    sortedList.appendChild(option);
  }
}