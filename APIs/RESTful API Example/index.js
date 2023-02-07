const express = require("express");
const app = express();
const PORT = 3005;

app.listen(PORT, () => console.log(`Server is running on port ${PORT}`));

app.use(express.json());

app.get("/tshirt", (req, res) => {
  res.status(200).send({
    size: "Large",
    message: "T-Shirt",
  });
});

app.post("/tshirt/:id", (req, res) => {
  const { id } = req.params;
  const { logo } = req.body;

  if (!logo) {
    res.status(418).send({
      message: "Logo is required",
    });
  }

  res.send({
    tshirt: `T-Shirt with you ${logo} and ID of ${id}`,
  });
});
