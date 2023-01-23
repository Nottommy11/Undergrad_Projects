//YouTube Tutorial: https://youtu.be/_8gHHBlbziw

/*
//Sync code example

function otherFunct() {
  console.log("We are in otherFunct");
  console.log("Do some stuff");
}

console.log("Start");

otherFunct();

console.log("End");
*/

/*
console.log("Start");

setTimeout(() => {
  console.log("We are in the timeout");
}, 2000);

items = [1, 2, 3, 4, 5];

items.forEach((item) => {
  console.log(item);
});

console.log("End");
*/

/* 
//Async Callback code example

console.log("Start");

function loginUser(email, password, onSuccess, onFailure) {
  if (onFailure) {
    console.log("User has failed to login");
  }
  setTimeout(() => {
    onSuccess({ userEmail: email });
  }, 2000);
}

function getUserVideos(email, callback) {
  setTimeout(() => {
    callback(["video1", "video2", "video3"]);
  }, 3000);
}

function videoDetails(video, callback) {
  setTimeout(() => {
    callback("Title of the video");
  }, 2000);
}

//Gets into callback hell
const user = loginUser("thomas@email.com", 123456, (user) => {
  console.log(user);
  getUserVideos(user.userEmail, (videos) => {
    console.log(videos);
    videoDetails(videos[0], (title) => {
      console.log(title);
    });
  });
});

console.log("Finish");
*/

/* 
//Async Promise code example

console.log("Start");

function loginUser(email, password) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("Now we have the data");
      resolve({ userEmail: email });
    }, 2000);
  });
}

function getUserVideos(email) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(["video1", "video2", "video3"]);
    }, 3000);
  });
}

function videoDetails(video) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Title of the video");
    }, 2000);
  });
}

//Looks way better than callback hell
loginUser("thomas@email.com", 123456)
  .then((user) => getUserVideos(user.email))
  .then((videos) => videoDetails(videos[0]))
  .then((detail) => console.log(detail));
*/

/* 
//SYNC CODE EXAMPLE

console.log("Start");

const user = loginUser("thomas@email.com", 123456);
const videos = videoDetails(user.userEmail);

const yt = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log("Getting stuff from youtube");
    resolve({ videos: [1, 2, 3, 4, 5] });
  }, 2000);
});

const fb = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log("Getting stuff from facebook");
    resolve({ user: "Name" });
  }, 5000);
});

Promise.all([yt, fb]).then((result) => console.log(result));

console.log("Finish");
*/

//SYNC CODE EXAMPLE
console.log("Start");

function loginUser(email, password) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // console.log("Now we have the data");
      resolve({ userEmail: email });
    }, 1000);
  });
}

function getUserVideos(email) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(["video1", "video2", "video3"]);
    }, 2000);
  });
}

function videoDetails(video) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Title of the video");
    }, 5000);
  });
}

loginUser("thomas@email.com", 123456)
  .then((user) => getUserVideos(user.email))
  .then((videos) => videoDetails(videos[0]));
// .then((detail) => console.log(detail));

async function displayUser() {
  try {
    const loggedInUser = await loginUser("thomas@email.com", 123456);
    const videos = await getUserVideos(loggedInUser.userEmail);
    const detail = await videoDetails(videos[0]);
    console.log(detail);
  } catch (err) {
    console.log("We could not get the videos");
  }
}

displayUser();

console.log("Finish");
