import { connect } from 'mongoose';

/**
 * Create a connection with mongodb.
 */
export async function connectMongoDb(): Promise<void> {
	if (process.env.DB_CONN_STRING) {
		await connect(process.env.DB_CONN_STRING);
	} else {
		console.log('MongoDB uri not provided');
	}
}
