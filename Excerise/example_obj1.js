var person = {
    name: ['Bob', 'Smith'],
    age: 32,
    gender: 'male',
    interests: ['music', 'skiing'],
    bio: function() {
      return this.name[0] + ' ' + this.name[1] + ' is ' + this.age + ' years old. He likes ' + this.interests[0] + ' and ' + this.interests[1] + '.';
    },
    greeting: function() {
      return ('Hi! I\'m ' + this.name[0] + '.');
    }
  };

  console.log("calling interests array from object:",person.name[0]);
  console.log("Calling age interger from object:",person.name[1]);
  console.log("calling gender string from object:",person.gender);
  console.log("calling interests array from object:",person.interests[1]);
  console.log("calling bio function from object:",person.bio());
  console.log("Calling greeting fucnction from object:",person.greeting())