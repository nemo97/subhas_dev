const pluginWebc = require("@11ty/eleventy-plugin-webc");

const eleventySass = require("eleventy-sass");

const { DateTime } = require('luxon');

module.exports = function (eleventyConfig) {
	eleventyConfig.addPlugin(pluginWebc,{
        useTransform: true,
    });
    eleventyConfig.addPassthroughCopy("posts/**/*.jpg");
    eleventyConfig.addPassthroughCopy("posts/**/*.svg");
    eleventyConfig.addPassthroughCopy("posts/**/*.png");
    eleventyConfig.addPassthroughCopy("posts/**/*.gif");
    eleventyConfig.addPassthroughCopy("posts/**/*.webm");
        
    eleventyConfig.addPlugin(eleventySass);

    eleventyConfig.addFilter('readableDate', (dateObj) => {
        return DateTime.fromJSDate(dateObj, { zone: 'utc' }).toFormat(
          'dd LLL yyyy'
        );
    })

    eleventyConfig.addFilter('stringify', (data) => {
        console.log("Stringifying data:", data);
        return ""; // Using null and "\t" for pretty-printing with tabs
    });
};