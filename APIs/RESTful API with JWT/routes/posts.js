const router = require("express").Router();
const verify = require("./verifyToken");

router.get("/", verify, (req, res) => {
  //res.send(req.user);
  //User.findOne({ _id: req.user });
  res.json({
    posts: {
      title: "My first post",
      description: "Random data you shouldn't access",
    },
  });
});

module.exports = router;
