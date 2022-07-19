const dns = require("dns");

dns.lookup("google.com", null, (err, addresses) => {
  if (err) {
    console.error(err);
  } else {
    console.log(addresses);
  }
});
