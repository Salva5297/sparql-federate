var pathname = window.location.pathname;

const yasqe = YASQE(document.getElementById("yasqe-div"), {
  sparql: {
		showQueryButton: true,
		endpoint: "/sparql",
		requestMethod: "GET"
	}
});
const yasr = YASR(document.getElementById("yasr-div"), {
  //this way, the URLs in the results are prettified using the defined prefixes in the query
  getUsedPrefixes: yasqe.getPrefixesFromQuery,
  // Ordered list of enabled output plugins
});

yasqe.options.sparql.callbacks.complete = yasr.setResponse;
