db.users.insertOne({
  firstName: "Ludwig",
  lastName: "Beethoven",
  employeeId: "1008",
  email: "beethoven@me.com",
  dateCreated: new Date(),
});

db.users.findOne({ employeeId: "1008" });

db.users.updateOne(
  { firstName: "Wolfgang", lastName: "Mozart" },
  { $set: { email: "mozart@me.com" } }
);

db.users.findOne({ firstName: "Wolfgang", lastName: "Mozart" });

db.users.find(
  {},
  {
    _id: 0,
    firstName: 1,
    lastName: 1,
    email: 1,
  }
);
