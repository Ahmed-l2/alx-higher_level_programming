#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  const tasks = JSON.parse(body);
  const completedTasks = {};

  for (const task of tasks) {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  }

  console.log(completedTasks);
});
