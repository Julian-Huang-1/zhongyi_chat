// JavaScript代码可以放在<head>标签内或者外部的JavaScript文件中
function sendMessage() {
    var userInput = document.getElementById("userInput");
    var message = userInput.value;

    if (message.trim() !== "") {
        var chatbox = document.querySelector(".chatbox");
        var userMessage = document.createElement("div");
        userMessage.className = "message flex items-center justify-end mb-2";
        userMessage.innerHTML = `   
  <div class="bg-green-400 text-white rounded-lg py-2 px-4">${message}</div>
  <img src="./images/icons8-user-64.png" alt="User" class="avatar mr-2">
`;

        chatbox.appendChild(userMessage);
        userInput.value = "";

        // 模拟后端返回的回复
        // 发送请求到后端接口
        fetch("http://127.0.0.1:8000/chat/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "q": message
            })
        })
            .then(response => response.json())
            .then(data => {
                // 处理后端返回的响应数据
                var botMessage = document.createElement("div");
                botMessage.className = "message flex items-center justify-start mb-2";
                botMessage.innerHTML = `   <img src="./images/icons8-robot-60.png" alt="Robot" class="avatar mr-2">
        <div class="bg-gray-200 rounded-lg py-2 px-4">${data}</div>
      `;

                chatbox.appendChild(botMessage);
                chatbox.scrollTop = chatbox.scrollHeight;
            })
            .catch(error => {
                console.error("Error:", error);
            });
    }
}
function initChat() {
    fetch("http://127.0.0.1:8000/chat", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })
        .then(response => response.json())
        .then(data => {
            if (data == 'ok') {
                // 处理后端返回的响应数据
                var chatbox = document.querySelector(".chatbox");
                var messages = chatbox.querySelectorAll(".message");

                // 移除已有的聊天消息
                messages.forEach(function (message) {
                    chatbox.removeChild(message);
                });

                // 清空输入框的值
                var userInput = document.getElementById("userInput");
                userInput.value = "";

                // 添加初始聊天消息
                var initialMessage = document.createElement("div");
                initialMessage.className = "message flex items-center justify-start mb-2";
                initialMessage.innerHTML = `
    <img src="./images/icons8-system-64.png" alt="System" class="avatar mr-2">
        <div class="bg-green-600 text-white rounded-lg py-2 px-4">请把你的问题描述地越详细越好</div>
`;

                chatbox.appendChild(initialMessage);
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
}  
