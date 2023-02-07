const user = {
    name: "Piyush Sharma",
    designation: "Senior Software Engineer",
    company: "Infuse Consulting",
    hobbies: ["Reading", "Listening to music", "Collecting stamps"]
}

/**
 * Use destructuting to log the following
*/

const printUserProfile = () => {
    // Piyush Sharma is a Senior Software Engineer at Infuse Consulting. He likes Reading, Listening to music and Collecting stamps
    const {name, designation, company,hobbies, message = `${name} is a ${designation} at ${company}. He likes ${hobbies.slice(0, -1).join(', ')+' and '+hobbies.slice(-1)}`} = user;
    console.log(message);
}

printUserProfile()

