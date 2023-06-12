var path          = require('path');
var webpack       = require('webpack');
var BundleTracker = require('webpack-bundle-tracker')

require('dotenv').config({ path: './.env' }); 

module.exports = {
    context: __dirname,
    mode: 'development',
    entry: {
      app: './app/app.tsx',
    },
    resolve: {
        modules: [
            path.resolve('..', 'node_modules'),
        ],
    },
    devtool: 'inline-source-map',
    performance : {
        hints : false,
    },
    output: {
        path: path.resolve('./web/static/bundles/'),
        filename: '[name].js',
    },
    plugins: [
        new webpack.DefinePlugin({
            'process.env': JSON.stringify(process.env),
        }),
        new BundleTracker({ filename: './webpack-stats.json' }),
    ],
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.tsx?$/,
                loader: 'ts-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.s?[ac]ss$/i,
                use: ['style-loader', 'css-loader', 'sass-loader']
            },
            {
                test: /\.(png|jpe?g|gif|jp2|webp)$/,
                loader: 'file-loader',
                options: { name: 'images/[name].[ext]'},
                exclude: /node_modules/
            },
        ],
    },
    resolve: {
        extensions: [ '.tsx', '.ts', '.js' ]
    },
};