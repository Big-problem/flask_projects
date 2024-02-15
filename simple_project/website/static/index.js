function deleteNote(noteId){
    // send info to backend
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),       
    }).then((_res) => {
        // In this case, "/" means refreash the page
        window.location.href = "/";
    });
}