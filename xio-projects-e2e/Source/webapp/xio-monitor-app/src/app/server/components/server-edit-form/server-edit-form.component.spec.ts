import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ServerEditFormComponent } from './server-edit-form.component';

describe('ServerEditFormComponent', () => {
  let component: ServerEditFormComponent;
  let fixture: ComponentFixture<ServerEditFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ServerEditFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ServerEditFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
