console.log("App Initialized");

import { connectMongoDb } from './app/mongo/mongodb.utils';
import { read_csv } from './app/mongo/parse_csv/parse_csv';

connectMongoDb().then(
	async () => {
		console.log("MongoDB Connected");
		read_csv('anxiety.csv')
	},
).catch((err) => console.log(err));

