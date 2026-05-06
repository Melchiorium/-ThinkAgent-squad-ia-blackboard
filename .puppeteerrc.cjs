const { join } = require("path");

/**
 * Keep Puppeteer browsers inside the repository tree so Render can reuse
 * the installed browser at runtime after the build step.
 */
module.exports = {
  cacheDirectory: join(__dirname, ".cache", "puppeteer"),
};
