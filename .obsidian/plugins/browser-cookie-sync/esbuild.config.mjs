import esbuild from "esbuild";

const production = process.argv[2] === "production";

const context = await esbuild.context({
	entryPoints: ["src/main.ts"],
	bundle: true,
	// Obsidian API + Electron + Node 内置模块都由运行时提供，不打包进去
	external: [
		"obsidian",
		"electron",
		"@electron/remote",
		"node:*",
		"child_process",
		"crypto",
		"fs",
		"os",
		"path",
	],
	format: "cjs",
	target: "es2018",
	logLevel: "info",
	sourcemap: production ? false : "inline",
	treeShaking: true,
	outfile: "main.js",
	platform: "node",
});

if (production) {
	await context.rebuild();
	process.exit(0);
} else {
	await context.watch();
}
