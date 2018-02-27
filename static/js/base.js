function search() {
                var searchWord = document.getElementById("searchbox").value
                if (searchWord)
                    window.location = '/bookcity/search/'+searchWord

            }