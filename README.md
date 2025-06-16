# Steps
- Create the postID, questionTitle, and tag list
  ```js
  var table = document.getElementById("quickedittable");

  var objectsList = [];

  for (var i = 1; i < table.rows.length; i++) {
    var cells = table.rows[i].cells;

    var postID = cells[1].innerText;
    var questionTitle = cells[3].lastChild.firstChild.value;
    var tag = cells[5].firstChild.firstChild.value;

    objectsList.push({
      postID: postID,
      questionTitle: questionTitle,
      tag: tag,
    });
  }

  console.log(objectsList);
  ```

- Save to `og.json`
- Run `prepare.py` file to create `new.json`
- Run `change.py` file to change the tag and title and wait
