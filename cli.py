"""
Ephermal Lab Deployer
Author: Divyaranjan Sahoo
"""

import os
import subprocess
import click

LABS_DIR = "labs"

@click.group()
def cli():
    """
    Ephemeral Cloud Native Lab Deployer 🧪
    A CLI tool to manage security lab environments using Docker.
    """
    pass

@cli.command("list")
def list_labs():
    """Lists all available lab environments."""
    click.echo(click.style("📚 Available Labs:", fg="yellow", bold=True))
    try:
        lab_files = [f for f in os.listdir(LABS_DIR) if f.endswith((".yml", ".yaml"))]
        if not lab_files:
            click.echo("No labs found in the 'labs' directory.")
            return

        for lab_file in lab_files:
            lab_name = os.path.splitext(lab_file)[0]
            click.echo(f"  - {lab_name}")

    except FileNotFoundError:
        click.echo(click.style(f"❌ Error: The directory '{LABS_DIR}' was not found.", fg="red"))

@cli.command("start")
@click.argument("lab_name")
def start(lab_name):
    """Starts a specific lab environment in the background."""
    lab_file_path = os.path.join(LABS_DIR, f"{lab_name}.yml")

    if not os.path.exists(lab_file_path):
        click.echo(click.style(f"❌ Error: Lab '{lab_name}' not found.", fg="red"))
        click.echo(f"   (Looked for: {lab_file_path})")
        return

    click.echo(f"🚀 Starting lab: {click.style(lab_name, bold=True)}...")
    click.echo("⏳ Please wait, this may take several minutes if images need to be downloaded...")

    command = ["docker-compose", "-f", lab_file_path, "up", "-d"]

    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        click.echo(click.style(f"✅ Lab '{lab_name}' deployed successfully!", fg="green"))

        if "web-vuln" in lab_name or "juice-shop" in lab_name:
            click.echo("   - Access the Juice Shop at http://localhost:3000")
        elif "sql-injection" in lab_name or "dvwa" in lab_name:
            click.echo("   - Access DVWA at http://localhost")
        elif "android" in lab_name:
            click.echo("   - Connect to the device with: adb connect localhost:5555")
        elif "ids" in lab_name:
            click.echo("   - Get a shell in the attacker container with: docker exec -it attacker-lab /bin/sh")

    except subprocess.CalledProcessError as e:
        click.echo(click.style(f"🔥 Deployment failed for '{lab_name}'.", fg="red"))
        click.echo(e.stderr)
    except FileNotFoundError:
        click.echo(click.style("❌ Error: 'docker-compose' not found. Is it installed and in your PATH?", fg="red"))


@cli.command("stop")
@click.argument("lab_name")
def stop(lab_name):
    """Stops and removes all containers for a specific lab."""
    lab_file_path = os.path.join(LABS_DIR, f"{lab_name}.yml")

    if not os.path.exists(lab_file_path):
        click.echo(click.style(f"❌ Error: Lab '{lab_name}' not found.", fg="red"))
        return

    click.echo(f"🛑 Stopping lab: {click.style(lab_name, bold=True)}...")

    command = ["docker-compose", "-f", lab_file_path, "down"]

    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        click.echo(click.style(f"✅ Lab '{lab_name}' has been stopped and cleaned up.", fg="green"))
    except subprocess.CalledProcessError as e:
        click.echo(click.style(f"🔥 Failed to stop '{lab_name}'.", fg="red"))
        click.echo(e.stderr)
    except FileNotFoundError:
        click.echo(click.style("❌ Error: 'docker-compose' not found.", fg="red"))


@cli.command("status")
@click.argument("lab_name")
def status(lab_name):
    """Shows the status of containers for a specific lab."""
    lab_file_path = os.path.join(LABS_DIR, f"{lab_name}.yml")

    if not os.path.exists(lab_file_path):
        click.echo(click.style(f"❌ Error: Lab '{lab_name}' not found.", fg="red"))
        return

    click.echo(f"📊 Checking status for lab: {click.style(lab_name, bold=True)}...")
    command = ["docker-compose", "-f", lab_file_path, "ps"]

    try:
        subprocess.run(command, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        click.echo(click.style(f"❌ Could not get status for '{lab_name}'.", fg="red"))


@cli.command("cleanup")
def cleanup():
    """Removes all unused Docker networks, containers, and volumes."""
    click.echo(click.style("⚠️  WARNING: This will remove all stopped containers, all dangling images, and all unused networks and volumes.", fg="red", bold=True))
    if click.confirm("Are you sure you want to continue?"):
        command = ["docker", "system", "prune", "-af"]
        click.echo("🧹 Cleaning up Docker resources...")
        subprocess.run(command)
        click.echo(click.style("✅ Cleanup complete!", fg="green"))
    else:
        click.echo("Cleanup cancelled.")


if __name__ == "__main__":
    cli()
