import { Schema, model } from 'mongoose';

// Create an interface representing a document in MongoDB
export interface Abstract extends Document {
	id: string;
	title: string;
	abstract: string;
	theme: string;
}

// Create a Schema corresponding to the document interface
const schema = new Schema<Abstract>({
	id: String,
	title: String,
	abstract: String,
	theme: String,
});

// Create a Model
export const AbstractModel = model<Abstract>('Abstract', schema);

