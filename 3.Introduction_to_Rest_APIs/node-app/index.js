const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

// Root route
app.get("/", (req, res) => {
  res.send("Welcome to my REST API");
});

// GET
app.get('/users', (req, res) => {
  res.json({ message: 'Returning list of users' });
});

// POST
app.post('/users', (req, res) => {
  const newUser = req.body;
  res.json({ message: 'User created', user: newUser });
});

// PUT
app.put('/users/:id', (req, res) => {
  const userId = req.params.id;
  const updatedUser = req.body;
  res.json({ message: `User with ID ${userId} updated`, updatedUser });
});

// DELETE
app.delete('/users/:id', (req, res) => {
  const userId = req.params.id;
  res.json({ message: `User with ID ${userId} deleted` });
});

// Start server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
