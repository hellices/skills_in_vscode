export interface User {
  id: string;
  email: string;
  name: string;
  createdAt: Date;
}

export class UserService {
  private users: User[] = [];

  getUserById(id: string): User | null {
    return this.users.find(user => user.id === id) ?? null;
  }

  createUser(email: string, name: string): User {
    const user: User = {
      id: String(this.users.length + 1),
      email,
      name,
      createdAt: new Date()
    };
    this.users.push(user);
    return user;
  }
}
