const pluginWebc = require("@11ty/eleventy-plugin-webc");

const eleventySass = require("eleventy-sass");

module.exports = function (eleventyConfig) {
	eleventyConfig.addPlugin(pluginWebc,{
        useTransform: true,
    });
    eleventyConfig.addPlugin(eleventySass);
};