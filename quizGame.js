Bot.send("Please enter your 'FULL NAME' to start the game");
var name;
var erpId;
var playerEnteredChoice = 0;
var questionNumber = 0;
var api;
var status = 1;
var answer;
let usedQuestions = [];
var random = -1;
var score = 0;
var optionList;
var startTime;
let data = {};
let question;
 
function allLetter(inputtxt) {
    if (!/[^a-zA-Z ]/.test(inputtxt)) {
        return true;
    }
    else {
        return false;
    }
}
 
function pickRandom(optionList) {
    const index = Math.floor(Math.random() * 4);
    return index;
}
 
function sendQuestion() {
    question = api.results[questionNumber].question;
    question = question.replaceAll("&quot;", '"');
    question = question.replaceAll("&#039;", "'");
    question = question.replaceAll("&shy;", "-");
    question = question.replaceAll("&eacute;", "é");
    question = question.replaceAll("&oacute;", "ó");
    question = question.replaceAll("&lrm;", " ");
    Bot.send((questionNumber + 1) + ": " + question);
    optionList = api.results[questionNumber].incorrect_answers;
    random = pickRandom();
    answer = (api.results[questionNumber].correct_answer).toLowerCase();
    optionList.splice(random, 0, api.results[questionNumber].correct_answer);
    for (var j = 0; j < optionList.length; j++) {
        Bot.send(j + 1 + " : " + optionList[j]);
    }
    startTime = Date.now();
}
 
async function respond(inputText, timeup = false) {
    if (timeup) {
        Bot.send("Timeup");
        return;
    }
    if (status == 1) {
        name = inputText.toUpperCase();
        if (allLetter(name)) {
            Bot.send("Please enter your College ERP ID ( Example - 0201csds112 ) ");
            status = 2;
            return;
        }
        else {
            Bot.send("Please enter a valid name");
            return;
        }
    }
    else if (status == 2) {
        if (inputText.includes("0201")) {
            erpId = inputText;
        }
        else {
            Bot.send("Invalid Id,Try again");
            return;
        }
 
        Bot.send("Thanks for giving your details");
        Bot.send("Let's begin this quiz now");
        Bot.send("Choose in which field you want to attempt the quiz");
        Bot.send("Press 1 for General Knowledge");
        Bot.send("Press 2 for Entertainment : Books");
        Bot.send("Press 3 for Entertainment : Video Games");
        Bot.send("Press 4 for Sports");
        Bot.send("Press 5 for Science and Nature");
        Bot.send("Press 6 for Vehicles");
        Bot.send("Press 7 for Entertainment : Japanese Anime & Manga");
        Bot.send("Press 8 for Entertainment : Cartoon & Animations");
        Bot.send("Press 9 for Entertainment : Film");
        Bot.send("Press 10 for Entertainment : Music");
        status = 3;
    }
    else if (status == 3) {
        playerEnteredChoice = parseInt(inputText);
        var category;
        if (playerEnteredChoice == 1) category = 9;
        else if (playerEnteredChoice == 2) category = 10;
        else if (playerEnteredChoice == 3) category = 15;
        else if (playerEnteredChoice == 4) category = 21;
        else if (playerEnteredChoice == 5) category = 17;
        else if (playerEnteredChoice == 6) category = 28;
        else if (playerEnteredChoice == 7) category = 31;
        else if (playerEnteredChoice == 8) category = 32;
        else if (playerEnteredChoice == 9) category = 11;
        else if (playerEnteredChoice == 10) category = 12;
        else {
            Bot.send("Invalid Choice, Try again");
            return;
        }
        api = await CampK12.fetch("GET", "https://opentdb.com/api.php?amount=15&category=" + category + "&difficulty=easy&type=multiple");
        console.log(api);
        sendQuestion();
        status = 4;
    }
    else if (status == 4) {
        inputText = inputText.toLowerCase();
        const timeTaken = (Date.now() - startTime) / 1000;
        const inTime = timeTaken <= 30;
        let dataObj = {};
        dataObj.question = question;
        dataObj.time = timeTaken;
        dataObj.categoryChosen = playerEnteredChoice;
        dataObj.markedAnswer = inputText;
        data[questionNumber] = dataObj;
        if (inTime && inputText == (random + 1) || inputText == answer) {
            Bot.send(`Correct Answer, you took ${timeTaken} seconds`);
            score++;
            questionNumber++;
            if (questionNumber == 15) {
                status = "end";
                Bot.send("Thanks for playing");
                Bot.send("Your total score is " + score);
                await CampK12.fetch("GET", "https://docs.google.com/forms/d/e/1FAIpQLSdle2x22P7NuV6HOoHX96dqeIvtIBRPJMAmbk8ZYwIaVFNp6Q/formResponse?&entry.225820139=" + name + "&entry.1522661760=" + erpId + "&entry.175845000=" + score + "&entry.586061398=" + JSON.stringify(data));
                return;
            }
            else {
                Bot.send("Here comes your next question");
                sendQuestion();
            }
        }
        else if (inputText != (random + 1) || inputText != answer) {
            if (!inTime) Bot.send(`Times Up !! you took ${timeTaken} seconds`);
            else Bot.send("Wrong Answer");
            questionNumber++;
            if (questionNumber == 15) {
                status = "end";
                Bot.send("Thanks for playing");
                Bot.send("Your total score is " + score);
                await CampK12.fetch("GET", "https://docs.google.com/forms/d/e/1FAIpQLSdle2x22P7NuV6HOoHX96dqeIvtIBRPJMAmbk8ZYwIaVFNp6Q/formResponse?&entry.225820139=" + name + "&entry.1522661760=" + erpId + "&entry.175845000=" + score + "&entry.586061398=" + JSON.stringify(data));
                return;
            }
            else {
                Bot.send("Here comes your next question");
                sendQuestion();
            }
        }
    }
}
