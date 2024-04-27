
document.addEventListener("DOMContentLoaded", function() {
    var userImage = document.getElementById('userImage');
    var username = document.getElementById('username');
    var clicks = 0;
    var questionList = document.getElementById('questionList');
    var toggleQuestionsButton = document.getElementById('toggleQuestionsButton');
    var isVisible = false;
    var commentInput = document.getElementById('comment');
    var validateCommentButton = document.getElementById('validateCommentButton');
    var commentStatus = document.getElementById('commentStatus');
    var insultWords = ["Abentesma","Achavascado","Abécula","Alimária","Andrajoso","Barregã","Biltre","Cuarra","Cacóstomo","Estroso","Estólido", "Estultilóquio","Nefelibata","Néscio","Sevandija","Somítico","Tatibitate","Xexé","Cheché", "Xexelento"];
    var userInfo = document.getElementById('userData');
    var userImg = document.getElementById('uImage');

    // Mostrar/Esconder imagem ao clicar duas vezes
    if (userImage) {
        userImage.addEventListener('click', function() {
            clicks++;

            if (clicks === 2) {
                userImage.style.display = 'none';
                clicks = 0;
            }
        });
    }

    // Mostrar a imagem ao clicar no nome de usuário
    if (username && userImage) {
        username.addEventListener('click', function() {
            userImage.style.display = 'block';
        });
    }

    //Mostrar lista de questoes
    if (toggleQuestionsButton && questionList) {
        toggleQuestionsButton.addEventListener('click', function() {
            isVisible = !isVisible;

            if (isVisible) {
                questionList.style.display = 'block';
                toggleQuestionsButton.textContent = 'Esconder lista de Questões';
            } else {
                questionList.style.display = 'none';
                toggleQuestionsButton.textContent = 'Mostrar lista de Questões';
            }
        });
    }

    validateCommentButton.addEventListener('click', function() {
        var comment = commentInput.value.toLowerCase(); // Converter para minúsculas para comparar

        // Verificar se o comentário contém palavras insultuosas
        var containsInsult = insultWords.some(function(word) {
            return comment.includes(word);
        });

        if (!containsInsult) {
            commentStatus.textContent = "Comentário aceito";
        } else {
            commentStatus.textContent = "";
            commentInput.value = ""; // Limpar o campo de input
        }
    });




    if(userImg && userInfo) {
        userImg.addEventListener('click', function () {
            userInfo.style.display = 'block';
        });

        userImg.addEventListener('mouseleave', function () {
            userInfo.style.display = 'none';
        });
    }
});
